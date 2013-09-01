data.adicu.com
====================

This is the recommend means of setting up data.adicu.com for development.
First, you will need to pull in all the git submodules.

	git submodule init
	git submodule update

Next, install [vagrant](http://www.vagrantup.com/). Once vagrant is installed,
you can run `vagrant up`, and vagrant+puppet will provision the virtual
machine for you and start the application. You can point your browser to
[http://192.168.50.4](http://192.168.50.4) to see the running app.

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
