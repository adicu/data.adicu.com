import app.basic
import tornado.web
import lib.pg

import models.courses.courses as model
import models.courses.courses_functions as model_functions

class CoursesHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(model, model_functions)

    @tornado.web.asynchronous
    def get(self):
        recognized_arguments = self.valid_query_arguments(model_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", 0)
        page = self.get_int_argument("page", 0)
        if not queries:
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        self.pgquery.execute(queries, callback=self._finish)

    def _finish(self, response):
        if response:
            return self.api_response(response)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
