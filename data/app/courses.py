import app.basic
import models.courses as model
import tornado.web
import functools

class CoursesHandler(app.basic.BaseHandler):
    @tornado.web.asynchronous
    self.model = model
    self.model_functions = model_functions
    def get(self):
        acceptable = self.valid_query_arguements(self.model_functions)
        queries = self.get_arguments_as_dict(acceptable)
        if not len(queries):
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        model.do_sql(self.pg, queries, callback=self._finish)

    def _finish(self, response):
        if isinstance(response, dict):
            return self.api_response(response)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
