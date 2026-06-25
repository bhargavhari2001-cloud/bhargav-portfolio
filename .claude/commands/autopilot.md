---
description: Drive the full build → review → test loop autonomously, fixing and re-running until every gate passes clean
argument-hint: [the task or change to complete]
---

Take this task from start to verified-correct by LOOPING: build, run every quality gate, fix whatever they flag, and re-run — repeating until everything passes clean. Don't stop at the first failure, and don't declare it done until the gates are actually green.

Task: $ARGUMENTS

## The loop
Repeat these rounds until an exit condition below is met:

1. **Build / fix** — implement the task, or apply fixes for the findings from the previous round. Make the smallest change that addresses the issue at its ROOT.
2. **Gate — review** — review the diff for correctness, security, and simplification (as in `/review`). Collect findings.
3. **Gate — verify** — actually run the checks that exist: tests / build / lint, plus a real browser pass for UI changes (as in `/qa`). Capture real results — never assume a fix worked; prove it by re-running the check.
4. **Decide:**
   - All gates pass with **no must-fix findings and no failing checks** → exit, go to **Finish**.
   - Otherwise → list the remaining problems and loop back to step 1.

## Stopping conditions (so it can't spin forever)
Stop and hand back to me — don't keep churning — the moment ANY of these is true:
- **Solved** — gates are green. (the success exit)
- **No progress** — the same failure survives 2 fix attempts, or the count of problems isn't shrinking round over round.
- **Round cap** — 5 rounds reached.
- **Out of depth** — the next fix needs a decision only I can make, or a destructive / irreversible action.

Each round, briefly log: round #, what you changed, what each gate said, and whether the problem set got smaller. If you catch yourself thrashing (re-introducing old errors, or guessing), STOP and report.

## Guardrails
- Verify for real every round — re-run the failing check and see it pass; don't infer success from inspection.
- Never deploy, push to a remote default branch, force-push, or run a destructive command inside the loop without asking first.
- Fix root causes, not symptoms. If you're tempted to skip/suppress a test or comment out code to make a gate pass, STOP and surface it instead.

## Finish
- **Exited clean:** summarize what you built, how many rounds it took, what the gates verified, and anything left for me. Do NOT auto-ship — hand off to `/ship` and wait for my go-ahead.
- **Exited stuck:** report the remaining problem, everything you tried, and 2–3 concrete options for me to choose from.
