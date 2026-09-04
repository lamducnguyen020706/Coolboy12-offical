"""HHTECH audit runner — orchestration only.

This package collects context, calls the HHTECH (GPT-5.6 Luna) API under
hhtech/standards/audit-standard.md and hhtech/standards/patch-standard.md,
writes hhtech/auditreport.md and hhtech/patchprompt.md, and commits/pushes
exactly those two files.

It is not the auditor and not the implementation agent. It decides no
architectural truth and no finding severity; both come from Luna's response,
validated for shape only, never for substance.
"""
