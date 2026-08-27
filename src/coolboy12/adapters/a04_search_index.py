"""A-04 — Search index adapter boundary.

Blueprint §26.3a row A-4 (§12.15).

coolboy12 requires: structural questions in the author's vocabulary,
returning objects, paths, and provenance.

This boundary must not own the author vocabulary, provenance semantics, or
the no-synthesized-answer rule. Those are native and stay native.

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
