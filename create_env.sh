#!/bin/bash


## Requirements
## gcc, make, Python 2.5+, python-pip, virtualenv

## Instalation
## Create a virtualenv, and activate this: 

virtualenv -p python2.7 env
source env/bin/activate
pip2 install -r requirements.txt
uwsgi --socket 0.0.0.0:80 --protocol=http -w wsgi:app
# python polyhack_map_2016.py
