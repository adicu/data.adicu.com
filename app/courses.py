import app.basic

class CoursesHandler(app.basic.BaseHandler):
    def get(self):
        # this is a basic handler
        # key = self.get_argument("key") # to get query parameters. add a default parameter for optional parameters
        # the full list of gett'rs are: (defined in basic.py and web.py)
        # self.get_argument, self.get_bool_argument, self.get_int_argument, self.get_int_argument_range, self.get_arguments
        self.render('index.html', message="Hello World!")
        # for an api response
        # return self.api_response(dict(message="Hello World!"))
