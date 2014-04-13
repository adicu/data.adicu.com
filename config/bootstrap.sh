#!/usr/bin/env bash

# update everything
apt-get -y update

# install git
apt-get -y install git-core git

# install postgres
sudo apt-get install postgresql
#sudo -u postgres psql initdb -D /usr/local/pgsql/data
###NUKE DATABASE LOST USERS AND TABLES
sudo -u postgres psql -c "DROP OWNED BY adi";
sudo -u postgres psql -c "DROP ROLE adi";
#echo 'stuff is hapnen'
#sudo -u postgres psql dropuser adi
sudo -u postgres psql -c "CREATE USER adi WITH PASSWORD 'adi'";
/vagrant/dev/load_dev_dump.sh

# install redis
sudo apt-get -y install redis-server
redis-cli -n 1 sadd tokens 12345   # add test token to redis
redis-cli -n 1 sadd tokens integration_test   # add test token to redis

# install python
apt-get -y install python
apt-get -y install python-pip
apt-get -y install python-dev
apt-get -y install python-software-properties
apt-get -y install libpq-dev
sudo pip install -r /vagrant/config/requirements.txt
pip install flake8  # for local testing

# install vim
apt-get -y install vim

# install supervisord
command -v supervisord > /dev/null
if [ $? -ne 0 ]; then
    apt-get -y install supervisor
    cat > /etc/supervisor/conf.d/data.conf << EOF
[program:data]
directory=/vagrant/
command=/vagrant/scripts/start_server_supervisor.sh /vagrant/config/settings.dev
autostart=true
autorestart=true
EOF
    service supervisor stop
    sleep 3
    service supervisor start
fi
