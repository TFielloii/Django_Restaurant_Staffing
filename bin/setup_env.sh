#!/bin/bash

# Removes the old virtual environment
rm -rf venv

# Creates a new virtual environment
python -m venv venv

# Activates the virtual environment and installs requirements
activate() {
    . venv/Scripts/activate

    echo "Installing requirements to virtual environment."
    pip install -r requirements.txt
}

activate