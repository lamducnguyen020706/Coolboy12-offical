"""A-11 — Version-control adapter boundary.

Blueprint §26.3a row A-11 (§26.2e).

coolboy12 requires: file versioning, rollback, commit identity, integrity.

This boundary is authoritative for repository files and never for meaning
(I-85). It must not own the History Record, WSV-H, semantic history, or canon
state. A commit records that a file changed; a History Record records what
canonically changed, why, with whose approval, caused by what, and in which
session.

Artifact 029 establishes the boundary only. There is no implementation here,
no provider chosen, and no external dependency. The adapter contract set is
Artifact 444, implementation is 445, and enforcement is 447.

World Record package constructs — World Record, World Relationship Record,
World History Record, WSV, WSV-H — are World Record Model constructs and must
not be assumed as universal adapter or Record Model semantics (RMS I-102). A
boundary is shared mechanism; it never becomes shared meaning (I-103).
"""
