"""A-10 — Public viewer adapter boundary.

Blueprint §26.3a row A-10 (§27.5).

coolboy12 requires: page-by-page presentation of published artifacts, and
nothing else.

This boundary must not expose anything else — it stays bounded by the public
exposure set.

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
