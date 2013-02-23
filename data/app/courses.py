import app.basic
import models.courses as model
import tornado.web
import functools

class CoursesHandler(app.basic.BaseHandler):
    @tornado.web.asynchronous
    def get(self):
        get_arg = self.get_argument
        possible = model.possible_query_parameters
        queries = {q: get_arg(q, None) for q in possible if get_arg(q, None)}
        if not len(queries):
            return self.error(400, "Bad Request. No Arguments")
        model.do_sql(self.pg, queries, callback=self._finish)

    def _finish(self, cursor):
        if isinstance(cursor, dict):
            return self.api_response(cursor)
        else:
            return self.error(status_code=413,
                    status_txt="RESPONSE_TOO_LARGE")
