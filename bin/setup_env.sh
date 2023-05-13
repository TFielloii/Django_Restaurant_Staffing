#!/bin/bash

# Removes the old virtual environment
rm -rf venv

# Creates a new virtual environment
python -m venv venv

# Activates the virtual environment and installs requirements
echo "Installing requirements to virtual environment."
source venv/Scripts/activate
pip install -r requirements.txt