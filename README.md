
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


## Importing Dev Data

We use a partial dump of our data for quick-and-easy development. This gets
loaded on VM provision by our Vagrant setup scripts. It contains a small subset
and is not updated frequently, but is sufficient for most feature development
and bug squashing.


## Data Sources

We have 3 data sources currently:

1. Registrar data on courses (this does not include course descriptions). This
   is provided in JSON and XML formats, updated daily at 8am. Ask
   <infrastructure@adicu.com> for URLs if you need them.

2. Course descriptions, from CCIT. These we have a one-time dump of; we should
   negotiate with CCIT to get regular updates.

3. Housing data, from housing. These we have a one-time dump of; we should
   negotiate with CCIT to get regular updates.

If you need access to any of these data sources, email
<infrastructure@adicu.com>. We cannot give them out freely due to our current
agreement with the school, but if you have a good reason, we can work something
out. Otherwise, we prefer that all data access be done through the ADI API; we
can work with you to provide any features you need in most cases.


# app structure

```
|-- config/ (config settings and install scripts)
|-- README.md (This file)
|-- data/
    \
    |-- data.py (the executable for this application)
    |-- static/ (your static files, such as js, css, imgs)
    |-- tests/ (unittest scripts that should be used during development)
    |-- housing/ (files associated with housing endpoints)
    |-- auth/ (files associated with authentication and rate limiting)
    |-- lib/ (files used by multiple endpoints for query building)
```


