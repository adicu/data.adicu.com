import app.basic

class MainHandler(app.basic.BaseHandler):
    def get(self):
        return self.api_response(dict(message="Hello World!"))
