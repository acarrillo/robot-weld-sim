#!/bin/bash
set -e

sudo apt-get install python-qt4

virtualenv venv --python=python2.7
ln -s /usr/lib/python2.7/dist-packages/PyQt4 venv/lib/python2.7/site-packages/PyQt4
ln -s /usr/lib/python2.7/dist-packages/sip.x86_64-linux-gnu.so venv/lib/python2.7/site-packages/sip.x86_64-linux-gnu.so

. venv/bin/activate

pip install -e ipc
pip install -e viewer
pip install -e controller
pip install -e welder
pip install -e sensor
pip install -e common
