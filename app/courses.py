import app.basic
import models.courses as model
import lib.dbs as dbs

class CoursesHandler(app.basic.BaseHandler):
    def get(self):
        get_arg = self.get_argument
        possible = model.possible_query_parameters
        queries = {q: get_arg(q, None) for q in possible if get_arg(q, None)}

        sql_query, sql_params = model.build_sql_query(queries)
        sql_response = dbs.do_sql(sql_query, sql_params)
        
        if not len(queries):
            return self.error(400, "Bad Request. No Arguments")
        else:
    #def _finish(err,
            return self.api_response(queries)
