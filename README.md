
[![Build Status](https://travis-ci.org/adicu/data.adicu.com.png?branch=travis)](https://travis-ci.org/adicu/data.adicu.com)

data.adicu.com
---

This is the recommend means of setting up data.adicu.com for development.
First, you will need to pull in all the git submodules.

    git submodule init
    git submodule update

Next, install [vagrant](http://www.vagrantup.com/).
Once vagrant is installed, you can run `vagrant up`, and vagrant will provision the virtual machine for you.
The app will run automatically under [Supervisor](http://supervisord.org/).
You can point your browser to [http://localhost:5000](http://localhost:5000) to see the running app.

If anything is wrong, the following commands will help you diagnose the app:

    vagrant ssh
    sudo service supervisor stop
    cd /vagrant
    source config/settings.dev
    cd data
    python data.py

Take a look at the logs, in `/var/log/supervisor` as well.

##Importing Dev Data

    cd dev
    sh load_dev_dump.sh

# app structure

    |-- config/ (config settings and install scripts)
    |-- Procfile (Heroku instructions on how to run the application)
    |-- README.md (This file)
    |-- data/
        \
        |-- data.py (the executable for this application)
        |-- scripts/ (command line helper scripts; database start/stop scripts)
        |-- static/ (your static files, such as js, css, imgs)
        |-- tests/ (py.test scripts that should be used during development)
        |-- templates/ (html templates)

