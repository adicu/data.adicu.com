import tornado.web
import app.basic


class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.redirect("docs/Documentation")

class ProfileHandler(app.basic.BaseHandler):
    def get(self):
        if self.get_secure_cookie("user"):
            self.write(self.get_secure_cookie("_id"))
        else:
            self.write("You are not auth'd")


