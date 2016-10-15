#!/bin/bash


## Requirements
## gcc, make, Python 2.5+, python-pip, virtualenv

## Instalation
## Create a virtualenv, and activate this: 

virtualenv -p python2.7 env
source env/bin/activate
pip install -r requirements.txt
python run.py

