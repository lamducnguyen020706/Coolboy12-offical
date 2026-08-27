"""A-08 — Rendering adapter boundary.

Blueprint §26.3a row A-8 (§18.9).

coolboy12 requires: artifact model + authored material specification → page
images.

This boundary must not own the material specification, which is authored
(§18.9 rule 1).

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
