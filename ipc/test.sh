#!/bin/bash

virtualenv testenv
. testenv/bin/activate

pip install -e .
pip install -r test-requirements.txt

pylint -rn ipc
