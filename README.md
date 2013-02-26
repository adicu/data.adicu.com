data.adicu.com
====================

This is a suggested means of setting up data.adicu.com for development.
First and foremost, make sure you are using [virtualenv](http://www.virtualenv.org/en/1.9.X/#installation).
Then setup a directory as follows:

    mkdir data.adicu.com
    cd data.adicu.com
    virtualenv --no-site-packages .
    source bin/activate
    mkdir github
    git clone git@github.com:adicu/data.adicu.com.git github
    cd github
    sudo pip install -r requirements.txt

The purpose of this structure is to isolate the location of our source code from that
of virtualenv.

To set up your environment, we exclusively use environment variables. All of our connections
to databases, and 99% of our settings rely on environment variables. You can see a full
list of environment variables at

        github/conf/settings.example

It is left up to the developer to configure their development environment and include
all necessary variables. We are currently using Postgres, Mongo, and Redis for this
application, and it is left up to the developer to set theset databases up and configure
them for development.

From here on out, we will assume that we are in the github directory.

------------

Once you have your environment setup, to run the app all you need to do is:

    source config/settings.example
    python data/data.py

This app is deployed on heroku. To get access to heroku, first off install
heroku. :) Then ask Justin or Zach for access.

# app structure

    |-- bin (executable scripts we use for one off jobs, such as setting up databases)
    |-- conf/ (configs)
    |-- Procfile (Heroku instructions on how to run the application)
    |-- README.md (This file)
    |-- requirements.txt (All necessary python dependencies for this application)
    |-- data/
        \
        |-- data.py (the executable for this application)
        |-- app/ (request handlers; notably all inheriting from basic.py)
        |-- lib/ (generic library code; will *not* do any request handling; driver wrappers)
        |-- model/ (models to that intelligent about the format and shape data and how to query it)
        |-- scripts/ (command line helper scripts; database start/stop scripts)
        |-- templates/ (html templates)
        |-- static/ (your static files, such as js, css, imgs)
        |-- tests/ (py.test scripts that should be used during development)
