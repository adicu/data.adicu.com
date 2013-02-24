import app.basic
import tornado.web
import functools
import lib.pg

import models.courses as model
import models.courses_functions as model_functions

class CoursesHandler(app.basic.BaseHandler):
    self.model = model
    self.model_functions = model_functions
    self.pgquery = lib.PGQuery(self.pg, model)
    
    @tornado.web.asynchronous
    def get(self):
        acceptable = self.valid_query_arguements(self.model_functions)
        queries = self.get_arguments_as_dict(acceptable)
        if not len(queries):
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        pgquery.do_sql(queries, callback=self._finish)

    def _finish(self, response):
        if isinstance(response, dict):
            return self.api_response(response)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
