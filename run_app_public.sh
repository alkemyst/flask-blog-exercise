#!/bin/bash

source env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
flask run --host 0.0.0.0


