#!/usr/bin/env bash
# Deploy the portfolio to Vercel production with an automatic cache-busting build stamp.
# Usage:  ./deploy.sh
# Requires a Vercel token: put it in an untracked .env file as  VERCEL_TOKEN=...
# (or export VERCEL_TOKEN in your shell before running). The .env file is gitignored.
set -euo pipefail
cd "$(dirname "$0")"

# 0) load local secrets from the untracked .env file, if present
if [ -f .env ]; then
  set -a; . ./.env; set +a
fi
if [ -z "${VERCEL_TOKEN:-}" ]; then
  echo "ERROR: VERCEL_TOKEN is not set. Add it to .env (VERCEL_TOKEN=...) or export it." >&2
  exit 1
fi

# 1) fresh build id (timestamp) — must match the regex used below: b<digits>
BID="b$(date +%Y%m%d%H%M%S)"

# 2) stamp it into the page (the BUILD constant) and version.json
#    macOS/BSD sed in-place:
sed -i '' "s/var BUILD='b[0-9]*'/var BUILD='$BID'/" index.html
printf '{"build":"%s"}\n' "$BID" > version.json
echo "Stamped build: $BID"

# 3) deploy to production
VERCEL_TOKEN="$VERCEL_TOKEN" \
  npx --yes vercel@latest deploy --prod --yes --scope bhargavhari2001-5140s-projects

echo "Deployed build $BID — clients will auto-refresh to it."

# 4) snapshot this deploy to git + push to GitHub (version history per release).
#    git add -A respects .gitignore, so .env / *.token / *.bak / .vercel never get committed.
if git rev-parse --git-dir >/dev/null 2>&1; then
  git add -A
  if git diff --cached --quiet; then
    echo "Git: nothing changed since last commit."
  else
    git commit -q -m "Deploy $BID" && echo "Git: committed $BID."
  fi
  if git remote get-url origin >/dev/null 2>&1; then
    if git push -q origin HEAD; then echo "Git: pushed to GitHub."; else
      echo "WARN: git push failed (deploy still live). Pull/rebase and push manually." >&2; fi
  else
    echo "WARN: no git remote 'origin' set — skipped GitHub push." >&2
  fi
fi
