import app.basic
import tornado.web
import lib.pg
import functools

import models.courses.courses as model
import models.courses.courses_functions as model_functions

class AffairsHandler(app.basic.BaseHandler):
    #render html template

class StudentEventsHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(model, model_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")


class AlumniEventsHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(model, model_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")


class SocialMediaHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(model, model_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
