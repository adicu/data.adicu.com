import app.basic
import models.courses as model
import tornado.web

class CoursesHandler(app.basic.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        get_arg = self.get_argument
        possible = model.possible_query_parameters
        queries = {q: get_arg(q, None) for q in possible if get_arg(q, None)}
        if not len(queries):
            return self.error(400, "Bad Request. No Arguments")

        model.do_sql(self.pg, queries, callback=_finish)

    def _finish(self, response, error=None):
        if isinstance(response, dict):
            return self.api_response(response)
        else
            return self.error(status_code=413,
                    status_txt="RESPONSE_TOO_LARGE")
