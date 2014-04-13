#!/bin/sh

# create the database
sudo -u postgres dropdb data2
sudo -u postgres psql -c "create database data2 encoding='UTF8' 
lc_collate='en_US.utf8' lc_ctype='en_US.utf8' template=template0"; 
sudo -u postgres psql data2 -c "GRANT CONNECT ON DATABASE data2 TO adi;"

# load the dev dump
DEV_DUMP_PATH=/vagrant/dev/data_dump.sql 
sudo -u postgres psql data2 < $DEV_DUMP_PATH