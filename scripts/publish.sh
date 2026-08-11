#!/usr/bin/env bash
#
# publish.sh — one-click: verify build → commit → push → watch deploy.
#
# Builds the site locally (production config) to catch errors first, commits
# and pushes your changes to `main`, then watches the GitHub Actions run that
# deploys to GitHub Pages and reports success/failure.
#
# Usage:
#   scripts/publish.sh                      # commit ALL changes, default message
#   scripts/publish.sh -m "post: new note"  # custom commit message
#   scripts/publish.sh -m "fix" file1 dir2  # only stage the given paths
#   scripts/publish.sh --no-verify          # skip the local Hugo build check
#   scripts/publish.sh --no-watch           # push but don't wait for the deploy
#
# Requires: git, hugo (or ~/bin/hugo), and gh (for watching the deploy).
# Override the Hugo binary with HUGO_BIN=/path/to/hugo.
#
set -euo pipefail

MSG=""
VERIFY=1
WATCH=1
PATHS=()

usage() { sed -n '3,18p' "$0" | sed 's/^# \{0,1\}//'; exit "${1:-0}"; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--message) MSG="$2"; shift 2 ;;
    --no-verify)  VERIFY=0; shift ;;
    --no-watch)   WATCH=0; shift ;;
    -h|--help)    usage 0 ;;
    -*)           echo "Unknown option: $1" >&2; usage 1 ;;
    *)            PATHS+=("$1"); shift ;;
  esac
done

# Always operate from the repo root.
cd "$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)"

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# --- Is there anything to do? -------------------------------------------------
has_local_changes() { ! git diff --quiet || ! git diff --cached --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; }
unpushed_count() { git rev-list --count "@{u}..HEAD" 2>/dev/null || echo 0; }

if ! has_local_changes && [[ "$(unpushed_count)" == "0" ]]; then
  echo "✓ Nothing to do — working tree clean and branch up to date with remote."
  exit 0
fi

# --- Verify the production build ----------------------------------------------
if [[ "$VERIFY" == "1" ]] && has_local_changes; then
  HUGO="${HUGO_BIN:-}"
  if [[ -z "$HUGO" ]]; then
    if command -v hugo >/dev/null 2>&1; then HUGO="hugo"
    elif [[ -x "$HOME/bin/hugo" ]]; then HUGO="$HOME/bin/hugo"
    else echo "✗ hugo not found (set HUGO_BIN or use --no-verify)." >&2; exit 1; fi
  fi
  echo "▶ Building site (production) to verify…"
  HUGO_ENVIRONMENT=production HUGO_ENV=production "$HUGO" --gc --minify >/dev/null
  echo "✓ Build OK"
fi

# --- Stage + commit -----------------------------------------------------------
if has_local_changes; then
  if [[ ${#PATHS[@]} -gt 0 ]]; then
    git add -- "${PATHS[@]}"
  else
    git add -A
  fi
  if git diff --cached --quiet; then
    echo "• Nothing staged to commit."
  else
    [[ -n "$MSG" ]] || MSG="update site ($(date '+%Y-%m-%d %H:%M'))"
    git commit -q -m "$MSG"
    echo "✓ Committed: $(git rev-parse --short HEAD) — $MSG"
  fi
fi

# --- Push ---------------------------------------------------------------------
if [[ "$(unpushed_count)" == "0" ]]; then
  echo "✓ Nothing to push."
  exit 0
fi
echo "▶ Pushing to origin/${BRANCH}…"
git push -q origin "$BRANCH"
SHA="$(git rev-parse HEAD)"
echo "✓ Pushed $(git rev-parse --short HEAD)"

# --- Watch the deploy ---------------------------------------------------------
if [[ "$WATCH" == "0" ]]; then
  echo "↗ Skipped watching. Track it: gh run list"
  exit 0
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "↗ gh not installed — can't watch. Deploy is running on GitHub Actions."
  exit 0
fi

echo "▶ Waiting for the GitHub Pages deploy…"
RUN=""
for _ in $(seq 1 30); do
  RUN="$(gh run list -L 10 --json databaseId,headSha \
        -q ".[] | select(.headSha==\"$SHA\") | .databaseId" 2>/dev/null | head -1)"
  [[ -n "$RUN" ]] && break
  sleep 4
done
if [[ -z "$RUN" ]]; then
  echo "↗ Couldn't find the run yet. Check: gh run list"
  exit 0
fi

until [[ "$(gh run view "$RUN" --json status -q .status 2>/dev/null)" == "completed" ]]; do
  sleep 5
done
CONCL="$(gh run view "$RUN" --json conclusion -q .conclusion 2>/dev/null)"

case "$CONCL" in
  success)  echo "✅ Deployed successfully (run $RUN). Live shortly at your site." ;;
  cancelled) echo "⚠ Deploy run $RUN was cancelled (often superseded by a newer push)." ; exit 1 ;;
  *)        echo "❌ Deploy run $RUN finished: $CONCL"
            echo "   (If it's a 401/auth error, that's usually a transient GitHub incident — re-run: scripts/publish.sh --no-verify)" ; exit 1 ;;
esac
