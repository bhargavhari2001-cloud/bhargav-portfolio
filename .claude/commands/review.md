---
description: Staff-engineer review of your current changes — correctness, security, and simplification
argument-hint: [optional: path or what to focus on]
---

Review the current changes like a skeptical staff engineer who has to put their name on this. Be specific and honest — do NOT rubber-stamp.

Focus (optional): $ARGUMENTS

## Gather the diff
- If this is a git repo: review uncommitted changes (`git status`, `git diff`, `git diff --staged`). If the work is on a feature branch, also weigh the diff vs the base branch.
- If it's NOT a git repo: review the files named above, or the files changed most recently in this session.

## Review across these axes
1. **Correctness** — logic bugs, off-by-one, wrong conditionals, unhandled edge cases, error/empty/null states, races.
2. **Security** — untrusted input handling, injection (SQL/HTML/command), secrets in code, missing authz, unsafe deserialization, CSP/headers for web. Apply OWASP-Top-10 thinking, but only flag what's actually present.
3. **Simplification & reuse** — dead code, duplicated logic, an existing helper that already does this, an abstraction not earning its keep, something the platform/stdlib gives for free.
4. **Fit** — does it match the surrounding code's conventions, naming, and comment density?

## Output
Group findings by severity: **Must-fix**, **Should-fix**, **Nice-to-have**. For each:
- `file:line` — what's wrong — the concrete fix (show the corrected snippet when it helps).

End with a one-line verdict: ship as-is, ship after must-fixes, or rework. If you fixed anything trivial inline, list it. If the diff is genuinely clean, say so plainly — don't invent problems.
