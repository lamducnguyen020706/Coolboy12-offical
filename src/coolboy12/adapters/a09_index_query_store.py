"""A-09 — Index/query store adapter boundary.

Blueprint §26.3a row A-9 (§12.15).

coolboy12 requires: fast lookup and analytical projection over canonical
records.

This boundary must not own canonical state. It is read from canon, never
from the index: canonical records → projection → external store, and never
the reverse.

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
