#!/bin/bash
set -e

virtualenv venv --python=python2.7
. venv/bin/activate

pip install -e ipc
pip install -e viewer
pip install -e controller
pip install -e welder
pip install -e sensor
pip install -e common
