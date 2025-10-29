#!/usr/bin/env bash
set -euo pipefail

# Simple helper to ensure JHU CSSE repo data is present under data/raw/COVID-19
# Usage:
#   ./scripts/fetch_jhu_data.sh [clone|zip]
# Default: clone (shallow)

REPO_URL="https://github.com/CSSEGISandData/COVID-19.git"
DEST="data/raw/COVID-19"
METHOD="${1:-clone}"

echo "Ensure JHU CSSE data is available at: $DEST"

if [ -d "$DEST/csse_covid_19_data" ]; then
  echo "Data already present at $DEST — nothing to do."
  exit 0
fi

mkdir -p "$(dirname "$DEST")"

if [ "$METHOD" = "clone" ]; then
  echo "Cloning (shallow) $REPO_URL -> $DEST"
  git clone --depth 1 "$REPO_URL" "$DEST"
  echo "Done. If you want to save space, you can remove the git metadata with: rm -rf $DEST/.git"
  exit 0
fi

if [ "$METHOD" = "zip" ]; then
  echo "Downloading ZIP archive and extracting..."
  tmpdir=$(mktemp -d)
  trap 'rm -rf "$tmpdir"' EXIT
  curl -L -o "$tmpdir/COVID-19-master.zip" https://github.com/CSSEGISandData/COVID-19/archive/refs/heads/master.zip
  unzip -q "$tmpdir/COVID-19-master.zip" -d "$(dirname "$DEST")"
  mv "$(dirname "$DEST")/COVID-19-master" "$DEST"
  echo "Extracted to $DEST"
  exit 0
fi

echo "Unknown method: $METHOD. Use 'clone' or 'zip'." >&2
exit 2
