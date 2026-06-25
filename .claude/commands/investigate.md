---
description: Root-cause a bug with a structured method — evidence before fixes
argument-hint: [the bug or symptom]
---

Investigate this problem methodically. Resist the urge to fix before you understand it. Find the ROOT cause, not the first symptom.

Problem: $ARGUMENTS

## 1 — Reproduce & pin down
State the exact symptom: expected vs. actual, and the smallest reliable way to trigger it. If you can't reproduce it yet, say what you'd need to.

## 2 — Gather evidence
Read the relevant code, logs, errors, and recent changes. Quote the specific lines/output that matter. Don't speculate past what the evidence supports.

## 3 — Hypotheses
List the plausible causes, ranked by likelihood. For each, note the cheapest check that would confirm or rule it out.

## 4 — Test, cheapest first
Work down the list. Narrow with bisection / targeted logging / a minimal repro rather than guessing. Re-rank as evidence comes in.

## 5 — Root cause
State the actual root cause AND the evidence that proves it — not just "this line is wrong" but WHY it produces the symptom. If the trail runs cold, report what you've ruled out and the best next step.

## 6 — Fix & guard
Propose the minimal fix at the root (not a symptom patch). After fixing, verify the original repro is gone, and add a test or guard so it can't silently regress. Confirm before any risky or destructive step.
