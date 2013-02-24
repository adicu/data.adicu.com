import app.basic
import tornado.web
import lib.PGQuery as PGQuery

import models.courses as model
import models.courses_functions as model_functions

class CoursesHandler(app.basic.BaseHandler):
    self.pgquery = PGQuery(self.pg, model)
    
    @tornado.web.asynchronous
    def get(self):
        recognized_arguments = self.valid_query_arguements(model_functions)
        queries = self.get_arguments_as_dict(recognized_arguments)
        if not len(queries):
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        pgquery.execute(queries, callback=self._finish)

    def _finish(self, response):
        if isinstance(response, dict):
            return self.api_response(response)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
