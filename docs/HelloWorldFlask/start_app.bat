@echo off
setlocal

set SCRIPT_DIR=%~dp0
for %%I in ("%SCRIPT_DIR%..\..") do set REPO_ROOT=%%~fI

cd /d "%REPO_ROOT%"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
)

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install -r docs\HelloWorldFlask\requirements.txt

echo Starting persistent local Flask app...
python docs\HelloWorldFlask\app.py
