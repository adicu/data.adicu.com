#!/bin/sh

# create the database
sudo -u postgres createdb data2
sudo -u postgres psql data2 -c "GRANT CONNECT ON DATABASE data2 TO adi;"

# load the dev dump
sudo -u postgres psql data2 < dev_dump.sql


