#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install flask
python -c "import flask; print(flask.__version__)"

