import app.basic
import tornado.web
import lib.pg
import functools

from models.housing import room
from models.housing import room_functions
from models.housing import building
from models.housing import building_functions

class RoomHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(room, room_functions)

    @tornado.web.asynchronous
    @app.basic.format_api_errors
    @app.basic.validate_token
    def get(self):
        recognized_arguments = self.valid_query_arguments(room_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", None)
        page = self.get_int_argument("page", 0)
        pretty = self.get_bool_argument("pretty", None)
        jsonp = self.get_argument("jsonp", None)
        if not queries:
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        internal_callback = functools.partial(self._finish, pretty=pretty, jsonp=jsonp)
        self.pgquery.execute(queries, page=page, limit=limit, callback=internal_callback)

    def _finish(self, response, pretty=None, jsonp=None):
        if response:
            return self.api_response(response, pretty=pretty, jsonp=jsonp)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")

class BuildingHandler(app.basic.BaseHandler):
    pgquery = lib.pg.PGQuery(building, building_functions)

    @tornado.web.asynchronous
    @app.basic.format_api_errors
    @app.basic.validate_token
    def get(self):
        recognized_arguments = self.valid_query_arguments(building_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", None)
        page = self.get_int_argument("page", 0)
        pretty = self.get_bool_argument("pretty", None)
        jsonp = self.get_argument("jsonp", None)
        if not queries:
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        internal_callback = functools.partial(self._finish, pretty=pretty, jsonp=jsonp)
        self.pgquery.execute(queries, page=page, limit=limit, callback=internal_callback)

    def _finish(self, response, pretty=None, jsonp=None):
        if response:
            return self.api_response(response, pretty=pretty, jsonp=jsonp)
        else:
            return self.error(status_code=204,
                    status_txt="NO_CONTENT_FOR_REQUEST", pretty=pretty,
                    jsonp=jsonp)
