import app.basic
import models.courses as model
import tornado.web
import functools

class CoursesHandler(app.basic.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        acceptable = model.accepted_query_parameters
        queries = get_arguments_as_dict(acceptable)
        if not len(queries):
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        model.do_sql(self.pg, queries, callback=self._finish)

    def _finish(self, response):
        if isinstance(response, dict):
            return self.api_response(response)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
