#!/bin/bash

echo "importing postgres data into elasticsearch"

USER=$(id -un)
source /home/$USER/venv/bin/activate

SETTINGS_FILE=$1
source $SETTINGS_FILE

SCRIPTDIR=$(dirname $0)
DATADIR=$(dirname $SCRIPTDIR)/data

if [ -z $PYTHONPATH ]; then
    export PYTHONPATH=$DATADIR
else
    export PYTHONPATH=$PYTHONPATH:$DATADIR
fi

python $DATADIR/scripts/pg_es_import.py
