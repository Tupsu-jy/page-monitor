#!/bin/bash

# Enable error messages
set -e

# Check if the virtual environment already exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating a new one..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "Virtual environment found, activating it..."
    source venv/bin/activate
fi

# Run the Python script
echo "Starting the script"
python taskMonitor.py

# Exit the virtual environment
deactivate
