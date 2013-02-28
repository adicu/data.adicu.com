from app import basic
import tornado.web
import lib.pg
import functools

import models.courses.courses as model
import models.courses.courses_functions as model_functions

class CoursesHandler(basic.BaseHandler):
    pgquery = lib.pg.PGQuery(model, model_functions)

    @tornado.web.asynchronous
    @basic.format_api_errors
    @app.basic.validate_token
    def get(self):
        recognized_arguments = self.valid_query_arguments(model_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", 0)
        page = self.get_int_argument("page", 0)
        pretty = self.get_bool_argument("pretty", None)
        if not queries:
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        internal_callback = functools.partial(self._finish, pretty=pretty)
        self.pgquery.execute(queries, page=page, limit=limit, callback=internal_callback)

    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
