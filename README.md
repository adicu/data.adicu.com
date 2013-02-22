data.adicu.com
====================

To get started make sure you are using [virtualenv](http://www.virtualenv.org/en/1.9.X/#installation).
Once installed run

    virtualenv --no-site-packages .
    source bin/activate
    sudo pip install -r requirements.txt

To set up your environment, we use environment variables. An example has been
included for you in conf/settings.example. Once you have those setup, to run the
app all you need to do is:

    python app.py

This app is deployed on heroku. To get access to heroku, first off install
heroku. :) Then ask Justin or Zach for access.

# app structure

    |-- app.py (the executable for this app)
    |-- app/ (request handlers; notably all inheriting from basic.py)
    |-- conf/ (configs)
    |-- lib/ (generic library code; will *not* do any request handling)
    |-- model/ (some stupid models to help you form those sql queries)
    |-- scripts/ (command line helper scripts; database start/stop scripts)
    |-- templates/ (html templates)
    |-- static/ (your static files, such as js, css, imgs)
    |-- tests/ (py.test scripts that should be used during development)

Top level files should be: app.py, README.md, Procfile (for heroku), and
requirements
