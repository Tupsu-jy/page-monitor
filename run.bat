:: This is untested

@echo off
setlocal enabledelayedexpansion

:: Check if the virtual environment exists
if not exist venv (
    echo Virtual environment not found. Creating a new one...
    python -m venv venv
    call venv\Scripts\activate
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo Virtual environment found, activating it...
    call venv\Scripts\activate
)

:: Run the Python script
echo Starting the script
python taskMonitor.py

:: Deactivate the virtual environment
deactivate
