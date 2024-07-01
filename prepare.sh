#!/bin/bash

# Ensure pyenv is initialized
eval "$(pyenv init -)"

# Install Python 3.12 using pyenv if not already installed
if ! pyenv versions | grep -q "3.12"; then
    pyenv install 3.12
fi

# Create a new pyenv virtualenv for the project if it doesn't exist
if ! pyenv virtualenvs | grep -q "universities_3.12"; then
    pyenv virtualenv 3.12 universities_3.12
fi

# Activate the virtual environment
pyenv activate universities_3.12

# Ensure pip is up to date
pip install --upgrade pip

# Install required Python modules
pip install requests

# Run the Python script
python teste.py Cambridge Oxford

# Deactivate the virtual environment
pyenv deactivate