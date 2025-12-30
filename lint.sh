#!/bin/bash
source /opt/venv/bin/activate
black .
flake8 .
pylint app