@echo off
rem One-step launcher: creates a venv if needed, installs deps, starts the web UI.
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python 3 is required but was not found.
  pause
  exit /b 1
)

if not exist venv python -m venv venv
venv\Scripts\python -m pip install -q -r requirements.txt
venv\Scripts\python web.py
pause
