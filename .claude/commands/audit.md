# /audit

Run the HHTECH audit pipeline for one Roadmap artifact. This command is a thin wrapper: all
logic lives in the runner at `hhtech/audit_runner/`, invoked through the executable
`./hhtech/audit`. This command does not reimplement any of it.

## Input

Exactly one artifact ID, e.g. `/audit 042` or `/audit 42`. Accept only a single identifier.
`/audit`, `/audit foo`, `/audit 0`, `/audit 491`, and `/audit 42 extra` are all invalid — do not
try to interpret or repair them; pass whatever was given straight to the runner and let it
refuse. Do not invent a default artifact ID and do not accept more than one.

## Run

```bash
./hhtech/audit <artifact-id>
```

Pass exactly the artifact identifier given to `/audit`, nothing else. Run it from the repository
root.

## Behavior

The runner:

1. Collects Blueprint / RMS / Roadmap / target-file / git-state context for the artifact.
2. Calls GPT-5.6 Luna (HHTECH) to produce `hhtech/auditreport.md`.
3. If the verdict is `PATCH REQUIRED`, calls Luna a second time to produce
   `hhtech/patchprompt.md`; otherwise clears `hhtech/patchprompt.md`.
4. Commits and pushes exactly those two files to the current branch.

This command does not patch the audited artifact, does not invoke a second Claude session, does
not retry on failure, and does not do anything the runner itself did not do.

## Report

Report the runner's own final summary (artifact, verdict, audit report path, patch prompt path
or "cleared", commit hash, branch, push result) exactly as it printed it. Propagate the runner's
exit code as this command's result — do not report success if the runner exited non-zero, and do
not paper over a failure. If the runner failed, report its exact error line and the exit code;
do not retry it and do not attempt to fix the failure yourself as part of this command.

## Do not

- Do not call the HHTECH API directly from this command.
- Do not write `hhtech/auditreport.md` or `hhtech/patchprompt.md` yourself.
- Do not commit or push anything yourself — the runner owns its own commit/push.
- Do not run `/audit` more than once per invocation, and do not add a `--re-audit` mode; there is
  no session memory, and re-running `/audit <id>` later is the entire re-audit mechanism.
