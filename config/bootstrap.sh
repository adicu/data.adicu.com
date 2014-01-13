#!/usr/bin/env bash

# update everything
apt-get -y update

# install git
apt-get -y install git-core git

# install postgres
sudo apt-get -y install postgresql postgresql-contrib
sudo -u postgres psql -c "CREATE USER adi WITH PASSWORD 'adi'";
sudo -u postgres psql -c "CREATE DATABASE data2 WITH OWNER adi";

# install python
apt-get -y install python
apt-get -y install python-pip
apt-get -y install python-dev
apt-get -y install python-software-properties
apt-get -y install libpq-dev
sudo pip install -r /vagrant/config/requirements.txt

# install vim
apt-get -y install vim



