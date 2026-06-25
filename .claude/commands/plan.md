---
description: Interrogate a feature with forcing questions, then write a short, concrete plan before any code
argument-hint: [feature or task to plan]
---

You are acting as a skeptical product partner + planning lead. The goal: pressure-test the idea first, then produce a tight plan. Do NOT write implementation code in this command.

Feature / task: $ARGUMENTS

## Step 1 — Interrogate (do this first)
Ask the FEWEST forcing questions that would actually change the design (3–6 max). Cover only what's genuinely unclear:
- What's the real user problem? Who hits it, and how often?
- What's the simplest version that delivers most of the value? What can we cut?
- What's explicitly OUT of scope for this pass?
- What's the riskiest assumption, or what could break?
- Any constraints (existing patterns to reuse, perf, data, deadline)?

Skip questions the request already answers. Don't ask for the sake of asking. Wait for answers before Step 2.

## Step 2 — Plan (after answers)
Write a short plan, no fluff:
- **Goal** — one sentence.
- **Approach** — the chosen direction in 2–4 sentences; name one alternative you rejected and why.
- **Changes** — concrete files/areas to touch and what each change does.
- **Steps** — ordered; each independently shippable where possible.
- **Risks / unknowns** — what to watch, what could go wrong.
- **Out of scope** — what we're deliberately NOT doing.

Favor the smallest change that works. Reuse existing patterns over new abstractions. If the request is already crisp, keep Step 1 to one or two questions and move straight to the plan.
