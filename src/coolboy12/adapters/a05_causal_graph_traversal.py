"""A-05 — Causal-graph traversal adapter boundary.

Blueprint §26.3a row A-5 (§15.19).

coolboy12 requires: traverse declared model dependencies; find paths,
cycles, reachability.

This boundary must not own the edges. Those are Relationship Record and
Registry model definitions, and they remain coolboy12 architecture.

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
