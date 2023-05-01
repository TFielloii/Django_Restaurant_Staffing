#!/bin/bash

rm db.sqlite3
rm 

python -m venv venv

activate() {
    . venv/Scripts/activate
    echo "Installing requirements to virtual environment."
    pip install -r requirements.txt
}

activate