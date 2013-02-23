import app.basic

class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.render('index.html', message="Hello World!")
