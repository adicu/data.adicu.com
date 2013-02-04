conf directory
==============

this is used for infrastructure configs related to this application. 

* skeleton_app.nagios.cfg - also get added to the "export nagios" section of `~/export.sh`
* skeleton_app.nginx.conf - nginx includes get referenced by machine specific nginx files in `~infrastructure/nginx/`

If a static dataset (ie: a blacklist) is used in both environments, and is a small file (< 10K) it can go here
as a .dat file. If it is small enough to be a dozen entries it can be in settings.py, and if it is significantly
larger it should be an external resource added by a separate install script, or stored in an external
database on a per-environment basis

