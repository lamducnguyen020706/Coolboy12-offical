"""Refusal proofs for the Artifact 036 ordinal allocator.

Every failure path, and one property that matters more than any of them: a
refusal never degrades into an allocation. Artifact 036's invariant is
constitutional — *ordinals never reused, including after retirement* — so the
dangerous failure is not an error, it is an error that quietly resets a
frontier and hands back an ordinal that was already issued.

Each test therefore checks two things: that the operation refused, and that the
frontier is exactly where it was.
"""

from __future__ import annotations

import json

import pytest

from coolboy12.bootstrap import ordinal as ordinal_module
from coolboy12.bootstrap.identity import MAX_ORDINAL
from coolboy12.bootstrap.ordinal import (
    OrdinalAllocationError,
    OrdinalAllocator,
    OrdinalErrorCode,
)


@pytest.fixture
def record(tmp_path):
    return tmp_path / "ordinals.json"


@pytest.fixture
def allocator(record):
    return OrdinalAllocator.create(record)


def _refusal(callable_, *args):
    with pytest.raises(OrdinalAllocationError) as raised:
        callable_(*args)
    return raised.value


# ---------------------------------------------------------------------------
# The namespace key
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("partition", "kind"),
    [
        ("w", "CH"),  # lowercase partition
        ("X", "CH"),  # not one of the six
        ("WW", "CH"),  # not a single character
        ("", "CH"),
        ("W", "ch"),  # lowercase kind
        ("W", "C"),  # one character
        ("W", "CHA"),  # three characters
        ("W", ""),
        ("W", "C1"),  # not two letters
        ("W", "C-"),
    ],
)
def test_a_namespace_no_identity_could_carry_is_refused(allocator, partition, kind):
    """036 DECISION: the minimum check that keeps allocation safe.

    Opening a sequence under a key no identity could bear would strand those
    ordinals in a namespace nothing can ever name. The rules are Artifact
    035's, reached through its public constants rather than restated.
    """
    error = _refusal(allocator.allocate, partition, kind)

    assert error.code is OrdinalErrorCode.INVALID_NAMESPACE


@pytest.mark.parametrize("value", [None, 1, ("W",), b"W"])
def test_a_non_string_namespace_component_is_refused(allocator, value):
    assert _refusal(allocator.allocate, value, "CH").code is (
        OrdinalErrorCode.INVALID_NAMESPACE
    )
    assert _refusal(allocator.allocate, "W", value).code is (
        OrdinalErrorCode.INVALID_NAMESPACE
    )


def test_the_namespace_check_agrees_with_the_035_parser(allocator):
    """Anti-drift: 036 accepts a namespace exactly when 035 can parse one.

    Two modules with two independent notions of a well-formed kind code would
    eventually disagree, and the disagreement would show up as ordinals
    allocated under a key no identity can carry.
    """
    from coolboy12.bootstrap.identity import IdentityParseError, parse_identity

    probes = [
        ("W", "CH"), ("E", "CH"), ("I", "QQ"), ("R", "ZZ"),
        ("w", "CH"), ("X", "CH"), ("W", "ch"), ("W", "C"), ("W", "CHA"), ("W", "C1"),
    ]  # fmt: skip

    for partition, kind in probes:
        try:
            parse_identity(f"{partition}-{kind}-000001-Example")
        except IdentityParseError:
            parses = False
        else:
            parses = True

        try:
            allocator.allocate(partition, kind)
        except OrdinalAllocationError:
            allocates = False
        else:
            allocates = True

        assert parses is allocates, f"{partition}-{kind} disagrees between 035 and 036"


# ---------------------------------------------------------------------------
# The singleton
# ---------------------------------------------------------------------------


def test_the_wsv_singleton_namespace_has_no_allocator(allocator):
    """SOURCE-FROZEN: *WSV bears no per-instance ordinal* (RMS §5).

    036 DECISION: that is operationalised as no sequence at all, so asking
    refuses rather than returning ``1``. There is exactly one WSV, and its
    object identity is a reserved marker, not something allocated.
    """
    error = _refusal(allocator.allocate, "W", "WS")

    assert error.code is OrdinalErrorCode.NON_ALLOCATABLE_SINGLETON
    assert str(error.namespace) == "W-WS"


def test_refusing_the_singleton_creates_no_sequence_for_it(allocator, record):
    """A refused singleton must not leave a namespace behind to grow later."""
    for _ in range(5):
        _refusal(allocator.allocate, "W", "WS")

    assert allocator.namespaces() == ()
    assert json.loads(record.read_text(encoding="utf-8"))["namespaces"] == []
    assert allocator.highest_allocated("W", "WS") == 0


def test_the_singleton_rule_is_the_pair_not_the_kind_alone(allocator):
    """``WS`` outside the World partition is an ordinary namespace key.

    036 does not know what ``WS`` means anywhere — the Registry owns that. It
    reserves one pair, not one code.
    """
    assert allocator.allocate("E", "WS") == 1
    assert _refusal(allocator.allocate, "W", "WS").code is (
        OrdinalErrorCode.NON_ALLOCATABLE_SINGLETON
    )


# ---------------------------------------------------------------------------
# Exhaustion
# ---------------------------------------------------------------------------


def _at_frontier(record, frontier):
    record.write_text(
        json.dumps(
            {
                "version": 1,
                "namespaces": [
                    {"partition": "W", "kind": "CH", "highest_allocated": frontier}
                ],
            }
        ),
        encoding="utf-8",
    )
    return OrdinalAllocator(record)


def test_an_exhausted_namespace_refuses_deterministically(record):
    """It does not wrap, and it does not go looking for a gap to reuse."""
    OrdinalAllocator.create(record)
    allocator = _at_frontier(record, MAX_ORDINAL)

    for _ in range(3):
        error = _refusal(allocator.allocate, "W", "CH")
        assert error.code is OrdinalErrorCode.EXHAUSTED

    assert allocator.highest_allocated("W", "CH") == MAX_ORDINAL


def test_exhaustion_never_wraps_to_the_start(record):
    """The failure mode that would be catastrophic: 999999 → 1."""
    OrdinalAllocator.create(record)
    allocator = _at_frontier(record, MAX_ORDINAL)

    _refusal(allocator.allocate, "W", "CH")

    assert json.loads(record.read_text(encoding="utf-8"))["namespaces"] == [
        {"partition": "W", "kind": "CH", "highest_allocated": MAX_ORDINAL}
    ]


def test_one_namespace_exhausting_does_not_touch_another(record):
    OrdinalAllocator.create(record)
    allocator = _at_frontier(record, MAX_ORDINAL)

    _refusal(allocator.allocate, "W", "CH")

    assert allocator.allocate("W", "CO") == 1


# ---------------------------------------------------------------------------
# State corruption — every branch fails closed
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Initialization — exactly one winner, and never an overwrite
# ---------------------------------------------------------------------------


def test_creation_cannot_overwrite_a_record_even_if_the_existence_check_lies(
    record, monkeypatch
):
    """The TOCTOU window, closed at the only place it can be closed.

    An earlier revision checked ``path.exists()`` and then wrote through
    ``os.replace``, which overwrites unconditionally. Two steps with a gap: a
    second initializer could pass the check while the first was still writing,
    and then reset a record that already held allocations — reissuing ordinals
    that had been handed out.

    This forces the gap wide open by making the existence check always report
    "absent". Creation must still refuse, because it no longer asks: the
    exclusive open is what decides, and the kernel decides it atomically.
    """
    allocator = OrdinalAllocator.create(record)
    assert [allocator.allocate("W", "CH") for _ in range(3)] == [1, 2, 3]

    from pathlib import Path

    monkeypatch.setattr(Path, "exists", lambda self: False)
    error = _refusal(OrdinalAllocator.create, record)
    monkeypatch.undo()

    assert error.code is OrdinalErrorCode.STATE_CORRUPTION
    assert OrdinalAllocator(record).highest_allocated("W", "CH") == 3
    assert OrdinalAllocator(record).allocate("W", "CH") == 4


def test_creation_does_not_go_through_the_overwriting_write_path():
    """``_write`` replaces unconditionally, which is wrong for creation.

    Correct for advancing a frontier over a record that already exists, and
    precisely wrong for bringing one into existence. Creation must not reach
    it, or the exclusive open above would be decorative.
    """
    import ast
    import inspect
    import textwrap

    tree = ast.parse(textwrap.dedent(inspect.getsource(OrdinalAllocator.create)))
    called = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }

    assert "_write" not in called
    assert "replace" not in called
    assert "O_EXCL" in inspect.getsource(OrdinalAllocator.create)


def test_concurrent_creation_has_exactly_one_winner(tmp_path):
    """Eight real processes, one target path, one record.

    Not a sequential stand-in: initialization safety is a property of the
    filesystem call, so the test has to make the filesystem call from separate
    processes. Whichever the kernel admits creates the record; every other must
    refuse and change nothing.
    """
    import subprocess
    import sys
    import textwrap
    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path

    import coolboy12.bootstrap.ordinal as module

    record = tmp_path / "contested.json"
    script = tmp_path / "create_once.py"
    script.write_text(
        textwrap.dedent(
            """
            import sys
            sys.path.insert(0, sys.argv[1])
            from coolboy12.bootstrap.ordinal import (
                OrdinalAllocationError, OrdinalAllocator,
            )
            try:
                OrdinalAllocator.create(sys.argv[2])
                print("CREATED")
            except OrdinalAllocationError as error:
                print(error.code.value)
            """
        ),
        encoding="utf-8",
    )
    source_root = str(Path(module.__file__).parents[3])

    def contend(_):
        finished = subprocess.run(
            [sys.executable, str(script), source_root, str(record)],
            capture_output=True,
            text=True,
            check=True,
        )
        return finished.stdout.strip()

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(contend, range(8)))

    assert results.count("CREATED") == 1, f"not exactly one winner: {results}"
    assert set(results) == {"CREATED", OrdinalErrorCode.STATE_CORRUPTION.value}

    # The record is the untouched empty state — no loser wrote over the winner.
    assert json.loads(record.read_text(encoding="utf-8")) == {
        "version": 1,
        "namespaces": [],
    }
    assert OrdinalAllocator(record).allocate("W", "CH") == 1


def test_creation_over_a_populated_record_preserves_every_frontier(record):
    """Kept conceptually separate from the fresh-path race above.

    That one starts from nothing and tests who wins. This one starts from
    allocations already made and tests that a second initializer destroys none
    of them.
    """
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")
    allocator.allocate("W", "CH")
    allocator.allocate("E", "CH")
    before = record.read_text(encoding="utf-8")

    for _ in range(3):
        assert _refusal(OrdinalAllocator.create, record).code is (
            OrdinalErrorCode.STATE_CORRUPTION
        )

    assert record.read_text(encoding="utf-8") == before
    reopened = OrdinalAllocator(record)
    assert reopened.highest_allocated("W", "CH") == 2
    assert reopened.allocate("W", "CH") == 3
    assert reopened.allocate("E", "CH") == 2


def test_a_missing_record_is_a_failure_not_a_fresh_start(record):
    """The most dangerous silent reset there is.

    If absence meant "begin at 1", deleting the record would release every
    ordinal ever allocated. It raises instead, and beginning a record is a
    separate deliberate act.
    """
    error = _refusal(OrdinalAllocator, record)

    assert error.code is OrdinalErrorCode.STATE_CORRUPTION


def test_a_deleted_record_does_not_restart_the_sequence(record):
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")
    allocator.allocate("W", "CH")
    record.unlink()

    assert _refusal(allocator.allocate, "W", "CH").code is (
        OrdinalErrorCode.STATE_CORRUPTION
    )
    assert _refusal(OrdinalAllocator, record).code is OrdinalErrorCode.STATE_CORRUPTION


def test_creating_over_an_existing_record_is_refused(record):
    """Overwriting a record has the same effect as resetting every frontier."""
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")

    assert _refusal(OrdinalAllocator.create, record).code is (
        OrdinalErrorCode.STATE_CORRUPTION
    )
    assert OrdinalAllocator(record).highest_allocated("W", "CH") == 1


def _record_holding(partition="W", kind="CH", frontier=1):
    """A record with one namespace entry, built rather than hand-typed.

    The corrupt cases below vary exactly one field each. Writing them out as
    concatenated JSON string fragments is how a missing comma becomes a
    silently different fixture, so they are constructed instead.
    """
    return json.dumps(
        {
            "version": 1,
            "namespaces": [
                {"partition": partition, "kind": kind, "highest_allocated": frontier}
            ],
        }
    )


@pytest.mark.parametrize(
    ("payload", "why"),
    [
        ("", "empty file"),
        ("{", "truncated JSON"),
        ("not json at all", "not JSON"),
        ('["W-CH"]', "not an object"),
        ('{"namespaces": []}', "no version"),
        ('{"version": 2, "namespaces": []}', "a format this module does not know"),
        ('{"version": 1}', "no namespaces key"),
        ('{"version": 1, "namespaces": {}}', "namespaces is not a list"),
        ('{"version": 1, "namespaces": ["W-CH"]}', "an entry is not an object"),
        (_record_holding(partition="w"), "an entry has an unusable namespace"),
        (_record_holding(kind="WS"), "the singleton cannot have allocated anything"),
        (_record_holding(frontier=0), "a frontier below the first ordinal"),
        (_record_holding(frontier=1_000_000), "a frontier above the maximum"),
        (_record_holding(frontier="3"), "a non-integer frontier"),
        (_record_holding(frontier=True), "a boolean frontier"),
        (
            json.dumps(
                {
                    "version": 1,
                    "namespaces": [
                        {"partition": "W", "kind": "CH", "highest_allocated": 3},
                        {"partition": "W", "kind": "CH", "highest_allocated": 1},
                    ],
                }
            ),
            "the same namespace twice, so its frontier is ambiguous",
        ),
    ],
)
def test_a_malformed_record_blocks_allocation_and_is_never_repaired(
    record, payload, why
):
    """036 DECISION: fail closed. Never reset, never repair, never skip.

    Each of these could be "recovered from" by ignoring the bad part and
    carrying on, and every one of those recoveries lowers a frontier. Artifact
    019 §6 makes it a restart requirement too: step 2 is *"Verify authoritative
    persisted state is readable"*, which an allocator that invented a fresh
    record would silently defeat.
    """
    record.write_text(payload, encoding="utf-8")

    assert (
        _refusal(OrdinalAllocator, record).code is OrdinalErrorCode.STATE_CORRUPTION
    ), why


def test_a_corrupt_record_is_left_exactly_as_found(record):
    """Failing closed also means not writing over the evidence."""
    payload = '{"version": 1, "namespaces": "wrong"}'
    record.write_text(payload, encoding="utf-8")

    _refusal(OrdinalAllocator, record)

    assert record.read_text(encoding="utf-8") == payload


# ---------------------------------------------------------------------------
# Concurrency
# ---------------------------------------------------------------------------


def test_a_held_lock_refuses_rather_than_races(allocator, record):
    """036 DECISION: contention fails closed instead of blocking or retrying.

    Two processes reading the same frontier would both write ``n + 1`` and
    issue it twice, which is reuse. Refusing is recoverable; reuse is not.
    """
    lock = record.with_name(record.name + ".lock")
    lock.touch()

    error = _refusal(allocator.allocate, "W", "CH")

    assert error.code is OrdinalErrorCode.CONCURRENT_ALLOCATION
    assert allocator.highest_allocated("W", "CH") == 0

    lock.unlink()
    assert allocator.allocate("W", "CH") == 1


def test_a_refusal_before_the_lock_leaves_no_lock_behind(allocator, record):
    """The singleton is refused before the lock is ever taken.

    Named for what it actually covers. The singleton check runs above ``with
    self._locked()``, so this proves the early-exit path takes no lock — not
    that an in-lock failure releases one, which is the test below.
    """
    _refusal(allocator.allocate, "W", "WS")

    assert not record.with_name(record.name + ".lock").exists()
    assert allocator.allocate("W", "CH") == 1
    assert not record.with_name(record.name + ".lock").exists()


def test_every_failure_inside_the_lock_still_releases_it(tmp_path, monkeypatch):
    """The three refusals that happen while the lock is held.

    ``EXHAUSTED``, ``STATE_CORRUPTION`` and ``PERSISTENCE_FAILURE`` are all
    raised after ``with self._locked()`` has been entered. A lock left behind
    by any of them would wedge the namespace permanently — and because
    contention fails closed rather than waiting, a stale lock is not something
    a later call recovers from on its own.
    """
    import os

    def lock_of(record):
        return record.with_name(record.name + ".lock")

    # EXHAUSTED — raised after the record is read, inside the lock.
    exhausted = tmp_path / "exhausted.json"
    OrdinalAllocator.create(exhausted)
    allocator = _at_frontier(exhausted, MAX_ORDINAL)
    assert _refusal(allocator.allocate, "W", "CH").code is OrdinalErrorCode.EXHAUSTED
    assert not lock_of(exhausted).exists()

    # STATE_CORRUPTION — raised by the read itself, inside the lock.
    corrupt = tmp_path / "corrupt.json"
    OrdinalAllocator.create(corrupt)
    allocator = OrdinalAllocator(corrupt)
    corrupt.write_text("{ not json", encoding="utf-8")
    assert _refusal(allocator.allocate, "W", "CH").code is (
        OrdinalErrorCode.STATE_CORRUPTION
    )
    assert not lock_of(corrupt).exists()

    # PERSISTENCE_FAILURE — raised by the write, inside the lock.
    unwritable = tmp_path / "unwritable.json"
    allocator = OrdinalAllocator.create(unwritable)
    monkeypatch.setattr(os, "replace", _raises(OSError("device is full")))
    assert _refusal(allocator.allocate, "W", "CH").code is (
        OrdinalErrorCode.PERSISTENCE_FAILURE
    )
    monkeypatch.undo()
    assert not lock_of(unwritable).exists()

    # And the namespace is still usable afterwards, which a stale lock would
    # have made impossible.
    assert allocator.allocate("W", "CH") == 1


def _raises(error):
    """A stand-in that raises ``error`` whatever it is called with."""

    def refuse(*args, **kwargs):
        raise error

    return refuse


def test_concurrent_allocators_never_hand_out_the_same_ordinal(record, tmp_path):
    """The invariant under real parallelism: distinct, or an error. Never both.

    Several processes race for the same namespace. Whatever the mix of
    successes and refusals, no ordinal appears twice.
    """
    import subprocess
    import sys
    import textwrap
    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path

    import coolboy12.bootstrap.ordinal as module

    OrdinalAllocator.create(record)
    script = tmp_path / "race.py"
    script.write_text(
        textwrap.dedent(
            """
            import sys
            sys.path.insert(0, sys.argv[1])
            from coolboy12.bootstrap.ordinal import (
                OrdinalAllocationError, OrdinalAllocator,
            )
            try:
                print(OrdinalAllocator(sys.argv[2]).allocate("W", "CH"))
            except OrdinalAllocationError as error:
                print(error.code.value)
            """
        ),
        encoding="utf-8",
    )
    source_root = str(Path(module.__file__).parents[3])

    def race(_):
        finished = subprocess.run(
            [sys.executable, str(script), source_root, str(record)],
            capture_output=True,
            text=True,
            check=True,
        )
        return finished.stdout.strip()

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(race, range(8)))

    ordinals = [int(r) for r in results if r.isdigit()]
    assert len(ordinals) == len(set(ordinals)), (
        f"an ordinal was issued twice: {results}"
    )
    assert set(results) <= {str(n) for n in ordinals} | {
        OrdinalErrorCode.CONCURRENT_ALLOCATION.value
    }
    assert OrdinalAllocator(record).highest_allocated("W", "CH") == len(ordinals)


# ---------------------------------------------------------------------------
# Persistence failure
# ---------------------------------------------------------------------------


def test_an_unwritable_record_refuses_and_issues_nothing(record, monkeypatch):
    """An allocation that cannot be made durable was not made.

    The ordinal is written to disk before it is returned, so a persistence
    failure means the caller never sees a number — rather than receiving one
    the record does not know about, which the next start would issue again.
    """
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")

    def refuse(*args, **kwargs):
        raise OSError("device is full")

    monkeypatch.setattr("os.replace", refuse)

    error = _refusal(allocator.allocate, "W", "CH")

    assert error.code is OrdinalErrorCode.PERSISTENCE_FAILURE

    monkeypatch.undo()
    assert allocator.highest_allocated("W", "CH") == 1
    assert allocator.allocate("W", "CH") == 2


def test_a_failed_write_leaves_no_partial_record_behind(record, monkeypatch):
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")
    monkeypatch.setattr(
        "os.replace", lambda *a, **k: (_ for _ in ()).throw(OSError("x"))
    )

    _refusal(allocator.allocate, "W", "CH")
    monkeypatch.undo()

    assert list(record.parent.glob("*.writing")) == []
    assert json.loads(record.read_text(encoding="utf-8"))["namespaces"] == [
        {"partition": "W", "kind": "CH", "highest_allocated": 1}
    ]


def _fail_directory_sync(monkeypatch):
    """Make ``os.fsync`` fail for a directory descriptor and nothing else.

    This exercises the real path rather than a stand-in: the temporary file is
    written and synced for real, ``os.replace`` genuinely runs, and only the
    final directory synchronisation fails. Monkeypatching ``os.replace``
    instead would test a different, earlier failure point — which is why the
    pre-replace test above is kept separate.
    """
    import os
    import stat

    real_fsync = os.fsync

    def selective(descriptor):
        if stat.S_ISDIR(os.fstat(descriptor).st_mode):
            raise OSError("directory synchronisation failed")
        return real_fsync(descriptor)

    monkeypatch.setattr(os, "fsync", selective)


@pytest.mark.skipif(
    not ordinal_module._DIRECTORY_SYNC_ENFORCED,
    reason="this platform does not offer directory synchronisation, so the "
    "module neither attempts nor claims it",
)
def test_a_failed_directory_sync_refuses_after_the_replacement(record, monkeypatch):
    """The durability step that used to fail silently now refuses.

    An earlier revision caught this error and carried on while the surrounding
    documentation claimed the guarantee. Now the caller learns that the
    allocation was not made durable, and receives no ordinal.
    """
    allocator = OrdinalAllocator.create(record)
    assert allocator.allocate("W", "CH") == 1

    _fail_directory_sync(monkeypatch)
    error = _refusal(allocator.allocate, "W", "CH")

    assert error.code is OrdinalErrorCode.PERSISTENCE_FAILURE


@pytest.mark.skipif(
    not ordinal_module._DIRECTORY_SYNC_ENFORCED,
    reason="this platform does not offer directory synchronisation",
)
def test_a_candidate_lost_to_a_late_failure_is_never_reissued(record, monkeypatch):
    """The invariant that outranks tidiness.

    The replacement succeeded before the synchronisation failed, so ``2`` is
    already recorded and the caller never received it. It is permanently
    consumed. The next allocation is ``3`` — never ``2`` — because reissuing it
    is reuse, and a permanent gap is always the better failure.
    """
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")

    _fail_directory_sync(monkeypatch)
    _refusal(allocator.allocate, "W", "CH")
    monkeypatch.undo()

    # A genuinely reopened allocator, reading the record from disk.
    reopened = OrdinalAllocator(record)
    assert reopened.highest_allocated("W", "CH") == 2
    assert reopened.allocate("W", "CH") == 3


@pytest.mark.skipif(
    not ordinal_module._DIRECTORY_SYNC_ENFORCED,
    reason="this platform does not offer directory synchronisation",
)
def test_a_late_failure_leaves_the_record_intact_and_no_temporary_behind(
    record, monkeypatch
):
    """Cleanup after a replace must not touch the authoritative record."""
    allocator = OrdinalAllocator.create(record)
    allocator.allocate("W", "CH")

    _fail_directory_sync(monkeypatch)
    _refusal(allocator.allocate, "W", "CH")
    monkeypatch.undo()

    assert record.exists()
    assert list(record.parent.glob("*.writing")) == []
    assert json.loads(record.read_text(encoding="utf-8")) == {
        "version": 1,
        "namespaces": [{"partition": "W", "kind": "CH", "highest_allocated": 2}],
    }


def test_no_durability_failure_is_caught_and_discarded():
    """Static guard on the mismatch this patch removed.

    Neither writing method may contain a bare ``except OSError: pass`` or an
    ``except`` that returns — a swallowed persistence error is precisely how
    documentation comes to claim more than the code enforces.
    """
    import ast
    import inspect
    import textwrap

    for method in (OrdinalAllocator._write, OrdinalAllocator._fsync_directory):
        tree = ast.parse(textwrap.dedent(inspect.getsource(method)))
        for handler in [n for n in ast.walk(tree) if isinstance(n, ast.ExceptHandler)]:
            body = handler.body
            assert not all(isinstance(node, ast.Pass) for node in body), (
                f"{method.__name__} discards an exception"
            )
            assert not any(isinstance(node, ast.Return) for node in body), (
                f"{method.__name__} returns from an exception handler"
            )
            assert any(isinstance(node, ast.Raise) for node in body), (
                f"{method.__name__} has a handler that does not re-raise"
            )


def test_an_error_names_its_code_and_namespace(allocator):
    error = _refusal(allocator.allocate, "W", "WS")

    assert error.code is OrdinalErrorCode.NON_ALLOCATABLE_SINGLETON
    assert (error.namespace.partition, error.namespace.kind) == ("W", "WS")
    assert "NON_ALLOCATABLE_SINGLETON" in str(error)
    assert "W-WS" in str(error)
