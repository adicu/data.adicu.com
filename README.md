data.adicu.com
====================

To get started make sure you are using[virtualenv](http://www.virtualenv.org/en/1.9.X/#installation).
Once installed run

    virtualenv --no-site-packages .
    source bin/activate
    sudo pip install -r requirements.txt


# app structure

    |-- app.py (the executable for this app)
    |-- app/ (request handlers; notably all inheriting from basic.py)
    |-- conf/ (configs)
    |-- lib/ (generic library code; will *not* do any request handling)
    |-- scripts/ (command line helper scripts; database start/stop scripts)
    |-- tests/ (py.test scripts that should be used during development)

Top level files should be: executables (the main app), or a README.md.
