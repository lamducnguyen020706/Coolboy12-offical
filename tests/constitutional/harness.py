"""Constitutional test harness — Artifact 011.

The execution mechanism for constitutional checks. This file is the *how*.
The authoritative invariant register is the *what*, and it belongs to
Artifact 012 (``tests/constitutional/register.md``). **No invariant is
defined, listed, numbered, or interpreted here.**

SoT: DEV-ENV · Auth: none · Canon: n/a. A result produced by this harness is
evidence about an implementation check. It never redefines the Blueprint, the
RMS, Canon, the Registry, or any Record Model semantic — the execution
environment runs coolboy12 and does not define it (Blueprint §9.5, P-33), and
a dependency provides capability, never authority (P-31).

Two outcomes are kept strictly apart, because the Roadmap requires it
(artifact 011 Val, artifact 126 Val — *"testable or explicitly
not-yet-testable with a reason"*):

    the system violated the invariant
        -> a failure, reported as a failure

    no executable implementation can test the invariant yet
        -> not-yet-testable, carrying a stated reason, and never a pass

An unavailable check is never represented as a successful proof.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import NoReturn

import pytest

__all__ = ["not_yet_testable", "run_check"]


def not_yet_testable(entry: str, reason: str) -> NoReturn:
    """Mark ``entry`` as not yet executable, and say why.

    The check did not run. It is reported as skipped, which pytest counts
    separately from passes, so nothing here can be mistaken for proof that
    the invariant holds.

    Both arguments are required. An entry cannot be set aside without a
    stated reason, so a blank reason raises rather than quietly skipping.
    """
    if not entry.strip():
        raise ValueError("entry is required")
    if not reason.strip():
        raise ValueError(
            f"{entry}: a reason is required to mark an entry not-yet-testable"
        )
    pytest.skip(f"{entry}: not-yet-testable — {reason}")


def run_check(entry: str, check: Callable[[], bool]) -> None:
    """Run a constitutional ``check`` and report the result under ``entry``.

    ``check`` returns True when the invariant holds. Any other return value
    is a failure naming ``entry``.

    Exceptions are deliberately not caught. An unexpected error propagates
    and pytest reports it, because swallowing it would turn an unknown state
    into a silent pass.
    """
    if not entry.strip():
        raise ValueError("entry is required")
    result = check()
    if result is not True:
        pytest.fail(f"{entry}: check did not hold (returned {result!r})")
