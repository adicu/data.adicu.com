#!/bin/bash

source /vagrant/config/settings.dev

echo '--------------------------------------'
echo '    pep 8 complicance testing'
echo '--------------------------------------'

flake8 data/auth
flake8 data/errors
flake8 data/housing
flake8 data/tests
flake8 data/data.py

echo '--------------------------------------'
echo '    unit testing'
echo '--------------------------------------'
cd /vagrant/data && nosetests -sv tests/

