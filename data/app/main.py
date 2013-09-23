import tornado.web
import app.basic
import json

class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.redirect("docs/Documentation")

class ProfileHandler(app.basic.BaseHandler):
    def get(self):
        userstr = self.get_secure_cookie('user')
        if userstr:
            user = json.loads(userstr)
            self.write(user['token'])
        else:
            self.write("You are not auth'd")
