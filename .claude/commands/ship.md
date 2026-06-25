---
description: Ship the current change the way THIS project ships — adaptive, with a pre-ship gate
argument-hint: [optional: one-line summary of the change]
---

Ship the current change. Adapt to how THIS project actually ships — do not impose a workflow it doesn't use. Confirm before any outward-facing or hard-to-reverse action.

Summary (optional): $ARGUMENTS

## Step 1 — Pre-ship gate
- Run the project's tests and/or build if they exist (`package.json` scripts, Makefile, etc.). Report results honestly — if something fails, stop and surface it. If there are NO tests, say so explicitly; don't pretend there are.
- Re-read your own diff for anything left in by mistake: debug logs, secrets, commented-out code.

## Step 2 — Detect how this project ships, then do that
- **Has a deploy script or documented deploy command** (e.g. `./deploy.sh`, a `deploy` npm script, instructions in README/CLAUDE.md or memory): use that EXACT flow. Don't invent a new one.
- **Git repo with a remote + PR workflow**: create a feature branch (never commit straight to the default branch without asking), make a clean commit, push, open a PR with `gh` — clear title, what/why body. Follow any commit/PR conventions the repo documents (e.g. trailer lines).
- **Neither**: summarize what changed and ask how I want to ship it.

## Step 3 — Confirm
Before pushing, opening a PR, or deploying to production, show me exactly what you're about to do and wait for my go-ahead. After shipping, report the result (PR link, deploy URL, or build id) and anything to watch.
