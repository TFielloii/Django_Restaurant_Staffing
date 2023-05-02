#!/bin/bash

python -m venv venv

activate() {
    . venv/Scripts/activate
    echo "Installing requirements to virtual environment."
    pip install -r requirements.txt
}

activate