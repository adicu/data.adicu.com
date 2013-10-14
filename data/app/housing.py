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

    config = {
        'GET': {
            'params': app.basic.pg_function_params(room_functions, {
                'limit': {
                    'type': 'int',
                    'default': None
                },
                'page': {
                    'type': 'int',
                    'default': 0
                },
                'pretty': {
                    'type': 'bool',
                    'default': None
                },
                'jsonp': {
                    'type': 'string',
                    'default': None
                },
            }),
            'function': 'process_get'
        }
    }

    @tornado.web.asynchronous
    @app.basic.format_api_errors
    @app.basic.validate_token
    def process_get(self, params):
        recognized_arguments = self.valid_query_arguments(room_functions)

        limit = params['limit']
        page = params['page']
        pretty = params['pretty']
        jsonp = params['jsonp']

        queries = {query: params[query] for query in recognized_arguments if params[query]}

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

    config = {
        'GET': {
            'params': app.basic.pg_function_params(building_functions, {
                'limit': {
                    'type': 'int',
                    'default': None
                },
                'page': {
                    'type': 'int',
                    'default': 0
                },
                'pretty': {
                    'type': 'bool',
                    'default': None
                },
                'jsonp': {
                    'type': 'string',
                    'default': None
                },
            }),
            'function': 'process_get'
        }
    }

    @tornado.web.asynchronous
    @app.basic.format_api_errors
    @app.basic.validate_token
    def process_get(self, params):
        recognized_arguments = self.valid_query_arguments(building_functions)

        limit = params['limit']
        page = params['page']
        pretty = params['pretty']
        jsonp = params['jsonp']

        queries = {query: params[query] for query in recognized_arguments if params[query]}

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
