"""Unit tests for the Artifact 036 ordinal allocator.

Proves row 036's ``Val`` — *ordinals never reused, including after retire* —
and its ``Done`` — *allocation record durable*. Refusal proofs live in
``tests/negative/`` and boundary proofs in ``tests/boundary/``, per the suite
responsibilities Artifact 010 established.

Every kind code below is a namespace key and nothing more. The Registry owns
what a kind means (Blueprint §13.11, §9.4), and no test here asks.
"""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap

import pytest

from coolboy12.bootstrap.identity import MAX_ORDINAL, MIN_ORDINAL, format_object_id
from coolboy12.bootstrap.ordinal import Namespace, OrdinalAllocator


@pytest.fixture
def record(tmp_path):
    """A freshly created allocation record."""
    return tmp_path / "ordinals.json"


@pytest.fixture
def allocator(record):
    return OrdinalAllocator.create(record)


def test_a_namespace_allocates_from_one_upward(allocator):
    """035 DECISION, carried: ordinals are one-based, so the first is #1."""
    assert [allocator.allocate("W", "CH") for _ in range(3)] == [1, 2, 3]
    assert MIN_ORDINAL == 1


def test_each_partition_kind_pair_owns_its_own_sequence(allocator):
    """036 DECISION: the allocation namespace is ``(partition, kind)``.

    Three namespaces, three independent sequences — so ``W-CH-000001``,
    ``E-CH-000001`` and ``W-CO-000001`` name three different objects and may
    all exist at once. A single global counter, or one counter per partition,
    could not produce this.
    """
    assert allocator.allocate("W", "CH") == 1
    assert allocator.allocate("E", "CH") == 1
    assert allocator.allocate("W", "CO") == 1

    assert allocator.allocate("W", "CH") == 2
    assert allocator.allocate("E", "CH") == 2
    assert allocator.allocate("W", "CO") == 2


def test_the_kind_is_part_of_the_namespace_not_only_the_partition(allocator):
    """A partition-only counter would make the second call return 2."""
    allocator.allocate("W", "CH")
    assert allocator.allocate("W", "CO") == 1


def test_the_partition_is_part_of_the_namespace_not_only_the_kind(allocator):
    """A kind-only counter would make the second call return 2."""
    allocator.allocate("W", "CH")
    assert allocator.allocate("E", "CH") == 1


def test_an_ordinal_is_never_handed_out_twice(allocator):
    """Row 036's ``Val``, over a long run in interleaved namespaces."""
    issued = [
        (partition, kind, allocator.allocate(partition, kind))
        for _ in range(200)
        for partition, kind in (("W", "CH"), ("E", "CH"), ("W", "CO"))
    ]

    assert len(set(issued)) == len(issued) == 600


def test_the_frontier_only_ever_moves_upward(allocator):
    """Non-reuse is structural: nothing in the API lowers a frontier.

    Retirement therefore cannot release an ordinal — not because a check
    forbids it, but because the operation does not exist. Artifact 036 does not
    own the record lifecycle; it owns a number that only goes up.
    """
    frontiers = []
    for _ in range(10):
        allocator.allocate("W", "CH")
        frontiers.append(allocator.highest_allocated("W", "CH"))

    assert frontiers == sorted(frontiers) == list(range(1, 11))
    assert frontiers == sorted(set(frontiers))


def test_retiring_a_record_cannot_return_its_ordinal(allocator):
    """The scenario row 036 names: *never reused, including after retire*.

    Allocate three, let the second one's Record be retired by whatever owns
    its lifecycle, and ask for the next. It is 4. There is no call that could
    have made it 2 — see the boundary suite, which proves the API has none.
    """
    assert [allocator.allocate("W", "CH") for _ in range(3)] == [1, 2, 3]

    # Whatever retires W-CH-000002 does so elsewhere; the allocator is not told
    # and does not care, which is exactly why the ordinal cannot come back.
    assert allocator.allocate("W", "CH") == 4
    assert allocator.highest_allocated("W", "CH") == 4


def test_the_frontier_is_readable_without_consuming_anything(allocator):
    assert allocator.highest_allocated("W", "CH") == 0

    allocator.allocate("W", "CH")
    assert [allocator.highest_allocated("W", "CH") for _ in range(5)] == [1] * 5
    assert allocator.allocate("W", "CH") == 2


def test_an_untouched_namespace_has_a_zero_frontier(allocator):
    """Zero is a frontier, never an ordinal: nothing has been allocated yet."""
    assert allocator.highest_allocated("I", "QQ") == 0
    assert allocator.namespaces() == ()


def test_the_record_lists_the_namespaces_it_has_allocated_into(allocator):
    allocator.allocate("W", "CH")
    allocator.allocate("E", "CH")

    assert allocator.namespaces() == (Namespace("W", "CH"), Namespace("E", "CH"))
    assert str(Namespace("W", "CH")) == "W-CH"


def _src() -> str:
    """The repository's ``src`` root, for the subprocess to import from."""
    from pathlib import Path

    import coolboy12.bootstrap.ordinal as module

    return str(Path(module.__file__).parents[3])


def test_the_allocation_record_survives_a_real_restart(record, tmp_path):
    """Row 036's ``Done``: *allocation record durable*.

    A genuinely separate Python process allocates and exits; a second process
    reads the record from disk and continues from where the first stopped.
    Nothing is shared between them but the file — no object, no import state,
    no interpreter.
    """
    program = textwrap.dedent(
        """
        import sys
        sys.path.insert(0, sys.argv[1])
        from coolboy12.bootstrap.ordinal import OrdinalAllocator
        allocator = OrdinalAllocator(sys.argv[2])
        print(allocator.allocate("W", "CH"))
        """
    )
    script = tmp_path / "allocate_once.py"
    script.write_text(program, encoding="utf-8")
    source_root = _src()

    OrdinalAllocator.create(record)

    def run() -> int:
        finished = subprocess.run(
            [sys.executable, str(script), source_root, str(record)],
            capture_output=True,
            text=True,
            check=True,
        )
        return int(finished.stdout.strip())

    assert [run(), run(), run()] == [1, 2, 3]
    assert OrdinalAllocator(record).highest_allocated("W", "CH") == 3


def test_a_reopened_allocator_reads_the_frontier_from_disk(record):
    """No frontier is cached between instances, so none can disagree."""
    first = OrdinalAllocator.create(record)
    first.allocate("W", "CH")
    first.allocate("W", "CH")

    second = OrdinalAllocator(record)
    assert second.highest_allocated("W", "CH") == 2
    assert second.allocate("W", "CH") == 3

    # And the first instance sees it too, because neither holds a counter.
    assert first.highest_allocated("W", "CH") == 3
    assert first.allocate("W", "CH") == 4


def test_the_record_on_disk_is_readable_and_says_what_it_means(allocator, record):
    allocator.allocate("W", "CH")
    allocator.allocate("W", "CH")

    state = json.loads(record.read_text(encoding="utf-8"))
    assert state == {
        "version": 1,
        "namespaces": [{"partition": "W", "kind": "CH", "highest_allocated": 2}],
    }


def test_the_maximum_ordinal_is_allocatable(record):
    """999999 is a valid allocation, not the first refusal."""
    OrdinalAllocator.create(record)
    record.write_text(
        json.dumps(
            {
                "version": 1,
                "namespaces": [
                    {
                        "partition": "W",
                        "kind": "CH",
                        "highest_allocated": MAX_ORDINAL - 1,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    assert OrdinalAllocator(record).allocate("W", "CH") == MAX_ORDINAL == 999_999


def test_the_ordinal_is_an_int_and_035_renders_it(allocator):
    """036 owns which ordinal; 035 owns how it is written.

    The handoff row 036 sits on: an ``int`` comes out here and becomes a
    canonical object identity through Artifact 035's formatter, which this
    module does not reimplement.
    """
    ordinal = allocator.allocate("W", "CH")

    assert isinstance(ordinal, int)
    assert format_object_id(ordinal) == "000001"
    assert format_object_id(allocator.allocate("W", "CH")) == "000002"


def test_allocation_is_deterministic_given_the_record(record):
    """The same record, the same next ordinal — every time, in any instance."""
    OrdinalAllocator.create(record)
    OrdinalAllocator(record).allocate("W", "CH")

    assert {
        OrdinalAllocator(record).highest_allocated("W", "CH") for _ in range(20)
    } == {1}
