#!/usr/bin/env bash
# One-step launcher: creates a venv if needed, installs deps, starts the web UI.
set -e
cd "$(dirname "$0")"

PY=$(command -v python3 || command -v python || true)
if [ -z "$PY" ]; then
  echo "Python 3 is required but was not found." >&2
  exit 1
fi

[ -d venv ] || "$PY" -m venv venv
./venv/bin/python -m pip install -q -r requirements.txt
exec ./venv/bin/python web.py
