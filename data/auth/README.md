
#Authentication

We use [Flask-OAuth](https://github.com/mitsuhiko/flask-oauth) to abstract away the oauth procedures.
The redirect URI is set using the environemnt settings.

After authenticating, we create a record in postgres with their token and generate a [uuid](http://en.wikipedia.org/wiki/Universally_unique_identifier).
The uuid will serve as their token for accessing the API.


