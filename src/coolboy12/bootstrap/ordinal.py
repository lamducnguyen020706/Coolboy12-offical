"""Ordinal allocator and allocation record — Artifact 036.

Artifact 036 · ``src/coolboy12/bootstrap/ordinal.py`` · Own: CONST · RM: all ·
T: code · R: IMPL · SoT: AUTHORITATIVE · Auth: allocating · Canon: n/a ·
CD: no · Ph/St: P1/1b · Req: BR-23 · BP: §13.9a · RMS: §5 · H: 035 · S: — ·
LS: — · G: — · → 037 · Val: ordinals never reused, including after retire ·
Done: allocation record durable · Why: identity permanence · Risk: high · ∥: no

What this module is
-------------------
The one place that decides which ordinal comes next, and the durable record of
what it has already decided::

    034  grammar, frozen
      ↓
    035  parse · format · identity-level resolution
      ↓
    036  allocate an ordinal · record it durably · never reuse it  ← here
      ↓
    037  structural validation

Row 036's ``Val`` is *ordinals never reused, including after retire* and its
``Done`` is *allocation record durable*. Those two clauses are the whole
artifact, and everything below exists to make them true rather than claimed.

The constitutional invariant
----------------------------
SOURCE-FROZEN. Blueprint §13.9a, on ``OBJECT_ID``: *"Stable ordinal. Never
reused, including after retirement, because history references it forever."*
RMS §5 states the same inside the frozen grammar: *"ordinals never reused
(including after retirement)"*. Artifact 034 §5.2 carries it and names this
artifact as the owner of the mechanism.

Non-reuse here is structural, not enforced by a check that could be removed.
Each namespace keeps one number — the highest ordinal ever allocated — and the
only operation that touches it moves it upward. There is no operation in this
module that lowers it, frees an ordinal, or hands back one already issued, so
reuse is not a case that is guarded against; it is a case that cannot be
expressed. **That is also why there is no retirement API here**: retirement
cannot release an ordinal if nothing can, and the record lifecycle belongs to
its Record Model, not to an allocator.

Why the record is AUTHORITATIVE
-------------------------------
Row 036 classifies this artifact ``SoT: AUTHORITATIVE``, and Artifact 016 §5
defines that class as *"This is where the fact lives. Not rebuildable; the fact
exists nowhere else."* The classification attaches to the **allocation
record** — the durable state — rather than to this source file, which is
``src/**`` like any other module.

The consequence is load-bearing: the allocation record must never be treated as
DERIVED. Rebuilding it by scanning existing Records would return the ordinals
of retired Records to circulation, which is precisely the reuse the invariant
forbids. It is not rebuildable, it is not a cache, and it has no second copy.

Where the record lives is not decided here
------------------------------------------
**Open item, reported rather than invented.** The Artifact 001 tree has no zone
for authoritative, non-canonical, non-rebuildable state: ``canon/**`` is
canonical data behind the Mutation Coordinator (Roadmap 152, not built),
``derived/**`` is rebuildable by definition, ``fixtures/**`` is TEMPORARY, and
``src/**`` is DEV-ENV code. No source names a home for an allocation record.

So this module does not choose one. :class:`OrdinalAllocator` requires the
record path from its caller and has no default, so nothing here writes into a
zone that no source has authorised. Siting the record is an authorial decision
and belongs with whichever artifact wires allocation into a running system.

What this module is not
-----------------------
Not a parser or formatter (Artifact 035), not the structural validator
(Artifact 037), not a Registry, not a Record store, not a lifecycle manager.
``Auth: allocating`` is the whole of its authority: it may decide an ordinal
and record that decision. It commits no canon — Spine law 2 routes canonical
mutation through the Mutation Coordinator, which is Roadmap 152 and does not
exist yet — and it stores no Record, no Record payload, and no semantic field.

It holds no kind roster and asks nothing about what a kind means. ``CH`` is a
namespace key here, and the Registry owns its meaning (Blueprint §13.11, §9.4).
"""

from __future__ import annotations

import json
import os
from contextlib import contextmanager
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

from coolboy12.bootstrap.identity import (
    KIND_LENGTH,
    MAX_ORDINAL,
    MIN_ORDINAL,
    PARTITIONS,
    WSV_SINGLETON,
)

if TYPE_CHECKING:
    from collections.abc import Iterator

__all__ = [
    "RECORD_VERSION",
    "Namespace",
    "OrdinalAllocationError",
    "OrdinalAllocator",
    "OrdinalErrorCode",
]


RECORD_VERSION: Final = 1
"""036 DECISION: the allocation record's format version.

Stamped on every write and required on every read. A record written by a later
format is refused rather than guessed at — misreading a frontier is how an
ordinal gets issued twice.
"""

_SINGLETON_NAMESPACE: Final = (WSV_SINGLETON.partition, WSV_SINGLETON.kind)
"""The one namespace that is not allocatable, taken from Artifact 035.

SOURCE-FROZEN, in two halves. RMS §5 records the accommodated variance —
*"WSV bears no per-instance ordinal — the grammar already admits a
singleton"* — and the kind code is ``WS`` per Blueprint §13.9a's World kind
table and RMS §8.1's frozen roster.

036 DECISION: that variance is operationalised as *no allocator at all* for
this namespace. There is no WSV sequence and no WSV counter; asking for one is
an error, not an allocation of ``000001``. The pair is read from
:data:`~coolboy12.bootstrap.identity.WSV_SINGLETON` rather than restated, so
the kind code exists in exactly one place in the repository.
"""

_DIRECTORY_SYNC_ENFORCED: Final = os.name == "posix"
"""Whether the containing directory is synchronised, and therefore claimed.

036 DECISION, and a capability question rather than a preference. Flushing the
directory entry is what makes the *replacement* durable as opposed to the
file's contents; POSIX provides it by opening the directory and syncing that
descriptor, and a platform that does not permit opening a directory cannot
offer it at all.

So the guarantee is stated conditionally and honestly: where this is true the
step is required and any failure refuses the allocation, and where it is false
the step is neither attempted nor claimed. No source names an operating
system — Artifact 014 fixes the environment boundary without naming one — so
this module does not narrow the supported platform by failing closed on a
capability the platform never had.
"""

_ALLOCATION_FLOOR: Final = MIN_ORDINAL - 1
"""The frontier of a namespace that has never allocated.

035 DECISION, carried: ordinals are one-based, so a namespace at ``0`` has
allocated nothing and its first allocation is :data:`MIN_ORDINAL`. ``0`` is a
frontier value and never an ordinal — and it is not the reserved singleton
marker either, which is a serialization of the *object identity*, not a count.
"""


class OrdinalErrorCode(StrEnum):
    """Why an allocation was refused.

    Every member below refuses. None of them degrades into an allocation, and
    none has a recovery path that could return a previously issued ordinal —
    a failure that silently becomes reuse is worse than a failure.
    """

    INVALID_NAMESPACE = "INVALID_NAMESPACE"
    """The partition or kind is not one an identity could carry."""

    NON_ALLOCATABLE_SINGLETON = "NON_ALLOCATABLE_SINGLETON"
    """The namespace is a singleton and has no ordinal sequence."""

    EXHAUSTED = "EXHAUSTED"
    """The namespace has allocated its highest representable ordinal."""

    STATE_CORRUPTION = "STATE_CORRUPTION"
    """The allocation record is missing, unreadable, or not what it claims."""

    PERSISTENCE_FAILURE = "PERSISTENCE_FAILURE"
    """The allocation could not be made durable, so it was not made."""

    CONCURRENT_ALLOCATION = "CONCURRENT_ALLOCATION"
    """Another allocation holds the record; this one refused rather than raced."""


class OrdinalAllocationError(Exception):
    """An allocation was refused, and no ordinal was issued.

    Carries an :class:`OrdinalErrorCode` and the namespace it concerns, so a
    caller can branch on the code rather than on message text.

    The guarantee that matters is what this exception means: when it is
    raised, the allocation did **not** happen and no ordinal left this module.
    A caller that sees it has not consumed anything.
    """

    def __init__(
        self,
        code: OrdinalErrorCode,
        message: str,
        *,
        namespace: Namespace | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.namespace = namespace
        where = f" [{namespace.partition}-{namespace.kind}]" if namespace else ""
        super().__init__(f"{code.value}: {message}{where}")


@dataclass(frozen=True, slots=True)
class Namespace:
    """One ordinal sequence: a partition and a kind.

    **036 DECISION — this is the allocation namespace.** Each ``(partition,
    kind)`` pair owns its own ordinals, so ``W-CH-000001``, ``E-CH-000001`` and
    ``W-CO-000001`` are three different objects that may all exist at once.

    This is a decision of the current build, not a Blueprint requirement, and
    is labelled that way deliberately. What the sources do say is consistent
    with it and worth recording: Blueprint §13.9a's own World kind table gives
    seven different kinds the example ordinal ``001`` — ``W-CH-001-Maximus``,
    ``W-CO-001-Democracy``, ``W-OR-001-Empire``, ``W-LI-001-DelPhonar``,
    ``W-SP-001-Human``, ``W-EV-001-…``, ``W-LO-001-Rome`` — which a single
    global or partition-wide counter could not produce. That is corroboration
    from an illustrative table, not a stated rule, so the decision stands as a
    decision.

    Holding partition and kind together also keeps the scope visible in every
    signature: an allocator that took a partition alone would be a different
    architecture, silently.
    """

    partition: str
    kind: str

    @property
    def is_allocatable(self) -> bool:
        """Whether this namespace has an ordinal sequence at all.

        False for the WSV singleton, which has one identity and no counter.
        """
        return (self.partition, self.kind) != _SINGLETON_NAMESPACE

    def __str__(self) -> str:
        return f"{self.partition}-{self.kind}"


def _namespace(partition: object, kind: object) -> Namespace:
    """Check a namespace key just far enough to allocate into it safely.

    **036 DECISION, deliberately minimal.** This is not a parser. Artifact 035
    owns parsing and Artifact 037 owns structural validation; what happens here
    is the smallest check that stops an allocation from opening a sequence
    under a key no identity could ever carry — which would strand those
    ordinals in a namespace nothing can name.

    The rules are Artifact 035's, reached through its public constants rather
    than restated, so the two cannot drift: the partition must be one of
    :data:`~coolboy12.bootstrap.identity.PARTITIONS` and the kind must be
    :data:`~coolboy12.bootstrap.identity.KIND_LENGTH` ASCII uppercase letters.

    Whether a kind *exists* is not asked. That is a Registry question
    (Blueprint §13.11, §9.4) and this module does not consult the Registry to
    hand out a number.
    """
    if not isinstance(partition, str) or not isinstance(kind, str):
        raise OrdinalAllocationError(
            OrdinalErrorCode.INVALID_NAMESPACE,
            "partition and kind must both be str",
        )
    if partition not in PARTITIONS:
        raise OrdinalAllocationError(
            OrdinalErrorCode.INVALID_NAMESPACE,
            f"partition must be one of {'/'.join(PARTITIONS)}, uppercase; got {partition!r}",
        )
    if not (
        len(kind) == KIND_LENGTH
        and kind.isascii()
        and kind.isalpha()
        and kind.isupper()
    ):
        raise OrdinalAllocationError(
            OrdinalErrorCode.INVALID_NAMESPACE,
            f"kind must be exactly {KIND_LENGTH} uppercase ASCII letters; got {kind!r}",
        )
    return Namespace(partition=partition, kind=kind)


class OrdinalAllocator:
    """The allocator, bound to one durable allocation record.

    Usage is two calls and no ceremony::

        allocator = OrdinalAllocator.create(path)   # once, deliberately
        ordinal = allocator.allocate("W", "CH")     # 1, then 2, then 3 …

    The ordinal comes back as an ``int``. **Rendering it is Artifact 035's
    job** — ``format_object_id(ordinal)`` gives ``"000001"`` — and this module
    neither reimplements that nor decides how many digits an object identity
    has. 036 owns *which* ordinal; 035 owns *how it is written*.

    Every instance reads and writes the record file on each call and keeps no
    cached frontier between them. That is the point rather than an oversight: a
    counter held in memory is a counter that disagrees with the record after a
    restart, and disagreeing about a frontier means issuing an ordinal twice.
    """

    __slots__ = ("_lock_path", "_record_path")

    def __init__(self, record_path: str | os.PathLike[str]) -> None:
        """Bind to an existing allocation record.

        :param record_path: the record's path. **Required, with no default.**
            No source names a zone for authoritative non-canonical state (see
            the module docstring), so this module refuses to pick one; an
            implicit path here would be this artifact quietly claiming a
            location in a tree Artifact 001 owns.

        :raises OrdinalAllocationError: ``STATE_CORRUPTION`` if no record
            exists at that path. **A missing record is a failure, not a fresh
            start.** Treating absence as "begin at 1" is exactly the silent
            reset that returns every previously issued ordinal to circulation,
            so creating a record is a separate, explicit act — see
            :meth:`create`.
        """
        self._record_path = Path(record_path)
        self._lock_path = self._record_path.with_name(self._record_path.name + ".lock")
        self._load()

    @property
    def record_path(self) -> Path:
        """Where this allocator's durable record lives."""
        return self._record_path

    @classmethod
    def create(cls, record_path: str | os.PathLike[str]) -> OrdinalAllocator:
        """Write a new, empty allocation record and bind to it.

        The one operation that may begin a frontier at zero, and it is
        deliberate, explicit, and refuses to run twice: if a record already
        exists at the path it raises rather than truncating, because
        overwriting an allocation record is indistinguishable in effect from
        resetting every namespace to ``000001``.

        :raises OrdinalAllocationError: ``STATE_CORRUPTION`` if a record is
            already there; ``PERSISTENCE_FAILURE`` if it cannot be written.
        """
        path = Path(record_path)
        if path.exists():
            raise OrdinalAllocationError(
                OrdinalErrorCode.STATE_CORRUPTION,
                f"an allocation record already exists at {path}; refusing to overwrite it, "
                f"because replacing a record resets every frontier and releases every "
                f"ordinal it held",
            )
        allocator = cls.__new__(cls)
        allocator._record_path = path
        allocator._lock_path = path.with_name(path.name + ".lock")
        allocator._write({"version": RECORD_VERSION, "namespaces": []})
        return allocator

    def allocate(self, partition: str, kind: str) -> int:
        """Allocate the next ordinal in ``(partition, kind)`` and record it.

        :param partition: one of the six partition codes.
        :param kind: a two-character uppercase kind code.
        :returns: the allocated ordinal, an ``int`` in
            :data:`MIN_ORDINAL`\\ ..\\ :data:`MAX_ORDINAL`.

        :raises OrdinalAllocationError: with the code naming the refusal —
            ``INVALID_NAMESPACE``, ``NON_ALLOCATABLE_SINGLETON``,
            ``EXHAUSTED``, ``STATE_CORRUPTION``, ``PERSISTENCE_FAILURE`` or
            ``CONCURRENT_ALLOCATION``. In every case no ordinal was issued.

        **036 DECISION — the ordinal is durable before it is returned.** The
        order is: take the lock, read the record, compute the next ordinal,
        write it durably, release, return. The write completes before the
        caller ever sees the number.

        This ordering is not a preference. Any other order admits the sequence
        *choose 7 → crash → next start chooses 7 again*, and that is reuse,
        which the invariant forbids absolutely. The cost is the opposite
        failure: a crash between the durable write and the caller's use of the
        ordinal leaves it consumed and unused — a permanent gap. **Gaps are
        accepted.** No source requires the sequence to be gapless, and the
        alternative to a gap is a reused ordinal.

        Nothing scans for gaps or looks for the lowest unused ordinal. Such a
        search would find exactly the ordinals of failed and retired records
        and hand them out again.
        """
        namespace = _namespace(partition, kind)
        if not namespace.is_allocatable:
            raise OrdinalAllocationError(
                OrdinalErrorCode.NON_ALLOCATABLE_SINGLETON,
                "this namespace is a singleton and has no ordinal sequence: it bears one "
                "identity, whose object identity is a reserved marker rather than an "
                "allocated ordinal (RMS §5). There is nothing here to allocate",
                namespace=namespace,
            )

        with self._locked():
            state = self._load()
            entries = state["namespaces"]
            entry = self._entry(entries, namespace)
            frontier = entry["highest_allocated"] if entry else _ALLOCATION_FLOOR

            if frontier >= MAX_ORDINAL:
                raise OrdinalAllocationError(
                    OrdinalErrorCode.EXHAUSTED,
                    f"namespace has allocated ordinal {MAX_ORDINAL}, the highest "
                    f"representable; it does not wrap and it does not reuse",
                    namespace=namespace,
                )

            ordinal = frontier + 1
            if entry is None:
                entries.append(
                    {
                        "partition": namespace.partition,
                        "kind": namespace.kind,
                        "highest_allocated": ordinal,
                    }
                )
            else:
                entry["highest_allocated"] = ordinal
            self._write(state)

        return ordinal

    def highest_allocated(self, partition: str, kind: str) -> int:
        """The frontier of a namespace: the highest ordinal ever allocated.

        Returns ``0`` for a namespace that has allocated nothing. Read-only —
        it allocates nothing and consumes nothing, and there is no companion
        setter, because a frontier that could be assigned is a frontier that
        could be lowered.
        """
        namespace = _namespace(partition, kind)
        entry = self._entry(self._load()["namespaces"], namespace)
        return entry["highest_allocated"] if entry else _ALLOCATION_FLOOR

    def namespaces(self) -> tuple[Namespace, ...]:
        """Every namespace the record has allocated into, in recorded order."""
        return tuple(
            Namespace(partition=entry["partition"], kind=entry["kind"])
            for entry in self._load()["namespaces"]
        )

    # -----------------------------------------------------------------------
    # The durable record
    #
    # 036 DECISION — format and mechanism. No source names a persistence
    # technology, so this is the smallest one that satisfies the row's
    # "allocation record durable" inside the repository's constraints:
    # Artifact 005 declares no runtime dependency, so the standard library is
    # the whole toolbox, and JSON is already the repository's machine-readable
    # format. No database, no schema migration framework, no event log.
    # -----------------------------------------------------------------------

    @staticmethod
    def _entry(
        entries: list[dict[str, Any]], namespace: Namespace
    ) -> dict[str, Any] | None:
        """The record entry for ``namespace``, or ``None``."""
        for entry in entries:
            if (
                entry["partition"] == namespace.partition
                and entry["kind"] == namespace.kind
            ):
                return entry
        return None

    def _load(self) -> dict[str, Any]:
        """Read the record, or refuse.

        **036 DECISION — fail closed, always.** Every path out of this method
        is either a record this module fully understands or an exception. There
        is no branch that returns an empty record, repairs a damaged one, or
        skips an entry it cannot read, because each of those silently lowers a
        frontier and releases the ordinals above it.

        Artifact 019 §6 makes this a restart requirement rather than a
        preference: step 2 of the cold-restart sequence is *"Verify
        authoritative persisted state is readable"*, and an allocator that
        invented a fresh record on an unreadable one would report a clean
        restart while having lost the frontier.
        """
        try:
            raw = self._record_path.read_text(encoding="utf-8")
        except FileNotFoundError as error:
            raise OrdinalAllocationError(
                OrdinalErrorCode.STATE_CORRUPTION,
                f"no allocation record at {self._record_path}. A missing record is not an "
                f"empty one: starting from zero here would reissue every ordinal ever "
                f"allocated. Use OrdinalAllocator.create() to begin one deliberately",
            ) from error
        except OSError as error:
            raise OrdinalAllocationError(
                OrdinalErrorCode.STATE_CORRUPTION,
                f"allocation record at {self._record_path} could not be read: {error}",
            ) from error

        try:
            state = json.loads(raw)
        except ValueError as error:
            raise OrdinalAllocationError(
                OrdinalErrorCode.STATE_CORRUPTION,
                f"allocation record at {self._record_path} is not valid JSON: {error}",
            ) from error

        return self._checked(state)

    def _checked(self, state: object) -> dict[str, Any]:
        """Require the record to be exactly the shape this module writes.

        A partially-understood record is refused rather than partially used.
        """

        def corrupt(detail: str) -> OrdinalAllocationError:
            return OrdinalAllocationError(
                OrdinalErrorCode.STATE_CORRUPTION,
                f"allocation record at {self._record_path} is malformed: {detail}",
            )

        if not isinstance(state, dict):
            raise corrupt("the record is not an object")
        if state.get("version") != RECORD_VERSION:
            raise corrupt(
                f"version is {state.get('version')!r}, and this module writes and reads "
                f"version {RECORD_VERSION}; guessing at another format risks reissuing an "
                f"ordinal"
            )
        entries = state.get("namespaces")
        if not isinstance(entries, list):
            raise corrupt("'namespaces' is not a list")

        seen: set[tuple[str, str]] = set()
        for entry in entries:
            if not isinstance(entry, dict):
                raise corrupt("a namespace entry is not an object")
            partition, kind = entry.get("partition"), entry.get("kind")
            frontier = entry.get("highest_allocated")
            try:
                namespace = _namespace(partition, kind)
            except OrdinalAllocationError as error:
                raise corrupt(
                    f"a namespace entry is unusable — {error.message}"
                ) from error
            if not namespace.is_allocatable:
                raise corrupt(
                    f"{namespace} is a singleton and can never have allocated an ordinal"
                )
            if isinstance(frontier, bool) or not isinstance(frontier, int):
                raise corrupt(f"{namespace} has a non-integer frontier {frontier!r}")
            if not MIN_ORDINAL <= frontier <= MAX_ORDINAL:
                raise corrupt(
                    f"{namespace} has frontier {frontier}, outside "
                    f"{MIN_ORDINAL}..{MAX_ORDINAL}"
                )
            if (namespace.partition, namespace.kind) in seen:
                raise corrupt(
                    f"{namespace} appears twice, so its true frontier is ambiguous"
                )
            seen.add((namespace.partition, namespace.kind))

        return {"version": RECORD_VERSION, "namespaces": entries}

    def _write(self, state: dict[str, Any]) -> None:
        """Replace the record atomically, and make it durable before returning.

        **What the source requires.** Row 036's ``Done`` is *allocation record
        durable*, and Artifact 019 §5 fixes the operational level: a restart is
        one in which *"the previous in-memory or runtime process state is
        assumed gone"* and the system is re-established *"from durable,
        persisted project state"*. That is survival of the loss of process
        memory, and no more. The words *power loss*, *fsync* and
        *crash-consistent* appear in no source, and Blueprint §12 states of the
        History Record that the constitution *"deliberately specifies no
        storage form, no schema, no serialization, no indexing, and no
        persistence strategy — those belong to implementation stages"*.

        **036 DECISION — this goes further than that, deliberately.** Write a
        sibling temporary file, flush and fsync it, replace atomically, then
        synchronise the containing directory. ``os.replace`` is atomic, so a
        reader sees the old record or the new one and never a half-written one.
        Non-reuse is constitutional and a torn or lost record is the one
        failure that cannot be repaired afterwards, so the stronger guarantee
        earns its cost.

        **What is claimed is exactly what is enforced.** Every step above
        raises on failure, none is swallowed, and a failure reaches the caller
        as ``PERSISTENCE_FAILURE`` with no ordinal returned. The one step that
        is conditional is the directory synchronisation, which is required
        where the platform offers it and neither attempted nor claimed where it
        does not — see :data:`_DIRECTORY_SYNC_ENFORCED`.

        **A late failure consumes the candidate, and that is correct.** If the
        replacement succeeds and the directory synchronisation then fails, the
        record on disk already carries the new frontier while the caller
        receives ``PERSISTENCE_FAILURE`` and no ordinal. The candidate is
        permanently consumed and becomes a gap. It is not rolled back: lowering
        a frontier to avoid a gap is the one repair that could reissue an
        ordinal after a crash, and a permanent gap is always preferable to
        that.
        """
        directory = self._record_path.parent
        temporary = self._record_path.with_name(self._record_path.name + ".writing")
        payload = json.dumps(state, indent=2, sort_keys=True) + "\n"

        try:
            with temporary.open("w", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, self._record_path)
            self._fsync_directory(directory)
        except OSError as error:
            # Safe after a successful replace too: the temporary path no longer
            # exists, so this is a no-op and never touches the record itself.
            temporary.unlink(missing_ok=True)
            raise OrdinalAllocationError(
                OrdinalErrorCode.PERSISTENCE_FAILURE,
                f"the allocation could not be made durable, so it was not made: {error}",
            ) from error

    @staticmethod
    def _fsync_directory(directory: Path) -> None:
        """Flush the directory entry, so the replacement itself is durable.

        Syncing the file makes its *contents* durable; syncing the directory is
        what makes the *rename* durable. Where the platform offers this the
        step is required, and every failure propagates to :meth:`_write` and
        reaches the caller as ``PERSISTENCE_FAILURE`` — nothing here is caught
        and discarded. An earlier revision swallowed these errors while the
        surrounding documentation claimed the guarantee they were meant to
        provide, which is the specific mismatch this method now exists to not
        have.

        Where :data:`_DIRECTORY_SYNC_ENFORCED` is false the platform cannot
        offer the step, so it is not attempted and the docstrings above do not
        claim it.
        """
        if not _DIRECTORY_SYNC_ENFORCED:
            return

        descriptor = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

    @contextmanager
    def _locked(self) -> Iterator[None]:
        """Hold exclusive access for one allocation, or refuse to race.

        **036 DECISION — one writer, and contention fails rather than waits.**
        The Blueprint settles the architecture this sits in: *"there is no
        permission model, no role-based access, and no concurrent-writer
        resolution"*, with the cost recorded as *"the system cannot become a
        studio tool without an amendment"*. So no distributed allocator is
        built here.

        A lock is still required, because read-modify-write is not atomic on
        its own: two processes reading frontier 3 would both write 4 and issue
        4 twice, and that is reuse. The mechanism is an exclusive-create lock
        file — standard library only, and portable, where an advisory file
        lock would not be — held for the microseconds of a single allocation.

        Contention raises ``CONCURRENT_ALLOCATION`` rather than blocking or
        retrying. A lock left behind by a crashed process therefore blocks
        allocation until a human removes it, and that is the intended
        direction: refusing to allocate is recoverable, and issuing an ordinal
        twice is not.
        """
        try:
            descriptor = os.open(self._lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError as error:
            raise OrdinalAllocationError(
                OrdinalErrorCode.CONCURRENT_ALLOCATION,
                f"another allocation holds {self._lock_path}. This refused rather than "
                f"raced; if no allocation is running, the lock is stale and removing it "
                f"is a deliberate act",
            ) from error
        except OSError as error:
            raise OrdinalAllocationError(
                OrdinalErrorCode.PERSISTENCE_FAILURE,
                f"the allocation lock at {self._lock_path} could not be taken: {error}",
            ) from error

        try:
            os.close(descriptor)
            yield
        finally:
            self._lock_path.unlink(missing_ok=True)

    def __repr__(self) -> str:
        return f"OrdinalAllocator(record_path={str(self._record_path)!r})"
