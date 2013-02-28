import tornado.web
import tornado.auth
import tornado.escape

import functools
import simplejson as json

import app.basic
import lib.auth as auth

class LoginHandler(app.basic.BaseHandler, tornado.auth.GoogleMixin):
    auth_user = auth.UserAuth()

    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        print user
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")
        self.auth_user.add_user(user, callback=self._on_save)
    
    def _on_save(self, response, error):
        if error:
             raise tornado.web.HTTPError(500, "Saving your info failed")
        response["_id"] = str(response["_id"])
        for key in response:
            self.set_secure_cookie(key, response[key])
        self.set_secure_cookie("user", json.dumps(response))
        self.redirect("/")

class LogoutHandler(app.basic.BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.write('You are now logged out. '
               'Click <a href="/">here</a> to log back in.')

