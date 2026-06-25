---
description: Verify the current change in a real browser using the preview tools, with proof
argument-hint: [optional: what to test]
---

QA the current change in a real browser. Use the `preview_*` tools only (never Bash or Chrome MCP for this). Don't ask me to check manually — verify it yourself and show proof.

What to test (optional): $ARGUMENTS

## Workflow
1. Ensure a dev server is running (`preview_start` if needed). For a static single-file site, start it on the project dir so `index.html` is served.
2. Reload if HMR isn't active (`preview_eval: window.location.reload()`).
3. Check for errors: `preview_console_logs`, `preview_logs`, `preview_network`.
4. `preview_snapshot` to confirm content/structure rendered.
5. Test the actual change: `preview_click` / `preview_fill` the relevant elements, then snapshot to confirm the result. If scroll or animation matters, exercise it.
6. `preview_resize` to check responsive layout + dark mode if layout/theme is involved.

## If you find a bug (loop until clean)
Read the source, fix it at the root, then re-verify from step 3. Keep looping until the page is clean — but STOP and report if the same bug survives 2 fixes, you've done 5 rounds, or a fix needs a decision only I can make. Never claim it's fixed without re-running the check and seeing it pass.

## Report
Share proof: `preview_screenshot` for visual changes, `preview_network` for API changes, `preview_logs` for server behavior. State clearly what you tested, what passed, and anything still broken.
