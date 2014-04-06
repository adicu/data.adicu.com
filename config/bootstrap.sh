#!/usr/bin/env bash

# update everything
apt-get -y update

# install git
apt-get -y install git-core git

# install postgres
sudo apt-get -y install postgresql postgresql-contrib
sudo -u postgres psql -c "CREATE USER adi WITH PASSWORD 'adi'";
/vagrant/dev/load_dev_dump.sh

# install redis
sudo apt-get -y install redis-server
redis-cli -n 1 del tokens
redis-cli -n 1 sadd tokens 12345   # add test token to redis
redis-cli -n 1 sadd tokens integration_test   # add test token to redis
redis-cli -n 1 sadd tokens local    # add test token to redis
redis-cli -n 1 del domains
redis-cli -n 1 sadd domains 127.0.0.1:5000  # add test domain to redis

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
