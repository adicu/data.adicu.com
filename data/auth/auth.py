
from flask import Blueprint, session, redirect, url_for
from flask_oauth import OAuth
from os import path, environ
import sys
import requests

import user

# add the parent directory for in-project imports
base_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

auth_blueprint = Blueprint('auth_blueprint', __name__)

GOOGLE_CLIENT_ID = environ['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = environ['GOOGLE_CLIENT_SECRET']
# one of the Redirect URIs from Google APIs console
REDIRECT_URI = environ['REDIRECT_URI']

GOOGLE_PEOPLE_URL = ("https://www.googleapis.com/oauth2/v1/userinfo?"
                     "access_token={token}")


oauth = OAuth()
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url=('https://accounts.google.com'
                                         '/o/oauth2/auth'),
                          request_token_url=None,
                          request_token_params={
                              'scope': ('https://www.googleapis.com'
                                        '/auth/userinfo.email'),
                              'response_type': 'code'
                          },
                          access_token_url=('https://accounts.google.com'
                                            '/o/oauth2/token'),
                          access_token_method='POST',
                          access_token_params={
                              'grant_type': 'authorization_code'
                          },
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)


@auth_blueprint.route('/login')
def login():
    callback = url_for('home', _external=True) + REDIRECT_URI
    return google.authorize(callback=callback)


@auth_blueprint.route('/'+REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']

    # get user info from Google People API
    profile = requests.get(GOOGLE_PEOPLE_URL.format(token=access_token))
    user_email, user_name = profile.json()['email'], profile.json()['name']

    # retrive/create user token
    user_token = user.get_user(user_email, user_name)
    session['token'] = user_token

    return redirect(url_for('home'))
