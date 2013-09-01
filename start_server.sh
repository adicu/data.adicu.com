#!/bin/bash

source ~/venv/bin/activate
source config/settings.$1
python data/data.py
