#!/bin/bash

# set up the environmental variables
# supervisord will not do this for us
source $1
<<<<<<< HEAD
python data/data.py # &

# start elasticsearch
sudo update-rc.d elasticsearch defaults 95 10
sudo /etc/init.d/elasticsearch start
=======
cd data
python data.py # &
>>>>>>> 5e93ef0b15673a5b6294807ead0374ce0a2e5458
