#!/bin/sh

# create the database
sudo -u postgres dropdb data2
sudo -u postgres createdb data2
sudo -u postgres psql data2 -c "GRANT CONNECT ON DATABASE data2 TO adi;"

# load the dev dump
DEV_DUMP_PATH=/vagrant/dev/dev_dump.sql
sudo -u postgres psql data2 < $DEV_DUMP_PATH


