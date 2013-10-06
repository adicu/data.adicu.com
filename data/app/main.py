import tornado.web
import app.basic
import json
import lib.auth as auth
import functools

class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.redirect("docs/Documentation")

class ProfileHandler(app.basic.BaseHandler):
    auth_token = auth.TokenAuth()

    def post_validate_token(self, valid, token):
        if valid:
            self.write(token)
        else:
            self.write("Your token is invalid, please log in again")
        self.finish()

    @tornado.web.asynchronous
    def get(self):
        userstr = self.get_secure_cookie('user')
        if userstr:
            user = json.loads(userstr)
            token = user['token']

            internal_callback = functools.partial(self.post_validate_token, token=token)
            self.auth_token.validate_token(token, callback=internal_callback)
        else:
            self.write("You are not auth'd")
            self.finish()
