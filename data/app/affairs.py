import app.basic
import tornado.web
import lib.pg
import functools

import models.affairs.student as student_model
import models.affairs.student_functions as student_functions

import models.affairs.alumni as alumni_model
import models.affairs.alumni_functions as alumni_functions

import models.affairs.social as social_model
import models.affairs.social_functions as social_functions

class AffairsHandler(app.basic.BaseHandler):
    #render html template

class StudentEventsHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(student_model, student_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)
        self.pgquery.execute(None, page=page, limit=limit, callback=internal_callback)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")


class AlumniEventsHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(alumni_model, alumni_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)
        self.pgquery.execute(None, page=page, limit=limit, callback=internal_callback)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")


class SocialMediaHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(social_model, social_functions)

    @tornado.web.asynchronous
    def get(self):
        pretty = self.get_bool_argument("pretty", None)
        internal_callback = functools.partial(self._finish, pretty=pretty)
        self.pgquery.execute(None, page=page, limit=limit, callback=internal_callback)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
