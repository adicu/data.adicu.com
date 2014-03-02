#!/bin/bash

# set up the environmental variables
# supervisord will not do this for us
source $1
cd data
python data.py # &
