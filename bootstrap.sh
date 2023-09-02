#!/bin/sh
export FLASK_APP=./flashcard/index.py
pipenv run flask --debug run -h 0.0.0.0
