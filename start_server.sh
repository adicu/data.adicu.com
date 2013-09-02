#!/bin/bash

# make sure to catch the SIGTERM signal
trap : SIGTERM

# set up the environmental variables
# supervisord will not do this for us
USER=$(id -un)
HOME=/home/$USER

# start the python program in the background
source $HOME/venv/bin/activate
source $1
python data/data.py &
FIND_PID=$!

# wait for the program to finish
wait $FIND_PID

# If the return value from wait was greater than 128,
# it means we caught a SIGTERM
# kill off the python program in that case
if [ $? -gt 128 ]; then
	echo "Stopping data.adicu.com application server"
	kill $FIND_PID
fi
