# Slim workflow commands

A lightweight, hand-rolled alternative to [gstack](https://github.com/garrytan/gstack) — just the spine, as plain Claude Code slash commands. No runtime, no install script, no global config rewrite. Each command is one markdown file you can read and edit.

The loop: **Plan → Build → Review → Test → Ship → Reflect** (with `/investigate` for when things break)

| Command | What it does |
|---------|--------------|
| `/autopilot`   | **The loop.** Builds → reviews → tests → fixes → re-runs, repeating until every gate passes clean (or it safely stops). (gstack `/autoplan`) |
| `/plan`        | Interrogates a feature with forcing questions, then writes a short concrete plan. (gstack `/office-hours`) |
| `/review`      | Staff-engineer review of your current diff — correctness, security, simplification. (gstack `/review` + `/cso`) |
| `/qa`          | Verifies the change in a real browser via the preview tools, with screenshots as proof. (gstack `/qa`) |
| `/ship`        | Runs a pre-ship gate, then ships the way *this* project ships (deploy script, or branch→PR). (gstack `/ship`) |
| `/investigate` | Root-causes a bug with a structured method — reproduce, evidence, hypotheses, fix + guard. (gstack `/investigate`) |
| `/reflect`     | Captures durable learnings from the session into your persistent memory. (gstack `/learn` + `/retro`) |

## The loop (`/autopilot`)
`/autopilot` runs the whole pipeline as a **convergence loop**: build → review → verify → fix → re-run, repeating until every gate passes clean. It only stops on one of four conditions, so it can't spin forever:
- **Solved** — gates are green.
- **No progress** — the same failure survives 2 fix attempts.
- **Round cap** — 5 rounds.
- **Out of depth** — the next step needs your decision or a risky action.

It verifies for real each round (re-runs the actual check, never assumes a fix worked) and never deploys or pushes on its own. `/qa` has the same loop-until-clean behavior for browser bugs. When it gets stuck, it stops and hands you the remaining problem plus options — it does not flail.

## Where these live
- **Personal:** `~/.claude/commands/` — available in every project.
- **Per-project:** copy any file into a repo's `.claude/commands/` to version it with the code (a project copy overrides the personal one of the same name).

## Editing
Each file has YAML frontmatter (`description`, `argument-hint`) and a prompt body. `$ARGUMENTS` is whatever you type after the command. Tweak freely — that's the point of keeping it slim.

## Adding more later
If you ever miss a gstack skill, lift its idea into a new `name.md` here. Candidates: `/careful` (warn before destructive ops), `/freeze` (restrict edits to one area while debugging), `/document` (sync docs to a change).
