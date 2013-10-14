from app import basic
import tornado.web
import lib.pg
import functools
from lib.elasticsearch import es_async

from models.courses_v2 import courses
from models.courses_v2 import courses_functions
from models.courses_v2 import sections
from models.courses_v2 import sections_functions

class FullTextSearchHandler(basic.BaseHandler):
    es_client = es_async()

    config = {
        'GET': {
            'params': {
                'q': {
                    'type': 'string',
                },
                'term': {
                    'type': 'string',
                    'default': None
                },
                'pretty': {
                    'type': 'bool',
                    'default': None
                },
                'jsonp': {
                    'type': 'string',
                    'default': None
                }
            },
            'function': 'process_get'
        }
    }

    @tornado.web.asynchronous
    @basic.format_api_errors
    @basic.validate_token
    def process_get(self, params):
        query = params['q']
        term = params['term']
        pretty = params['pretty']
        jsonp = params['jsonp']

        if term:
            actual_query = '%s AND Term:%s' % (query, term)
        else:
            actual_query = query

        internal_callback = functools.partial(self._ft_finish,
                pretty=pretty, jsonp=jsonp)
        self.es_client.search('courses', actual_query, internal_callback)

    def _ft_finish(self, result, pretty=None, jsonp=None):
        if 'hits' not in result:
            return self.error(status_code=404, status_txt="RESULTS NOT FOUND")
        norm_result = [hit['_source'] for hit in result['hits']['hits']]
        return self.api_response(norm_result, pretty=pretty, jsonp=jsonp)

class CoursesV2Handler(basic.BaseHandler):
    course_pgquery = lib.pg.PGQuery(courses, courses_functions)
    section_pgquery = lib.pg.PGQuery(sections, sections_functions)

    config = {
        'GET': {
            'params': basic.pg_function_params(courses_functions, {
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
    @basic.format_api_errors
    @basic.validate_token
    def process_get(self, params):
        recognized_arguments = self.valid_query_arguments(courses_functions)

        limit = params['limit']
        page = params['page']
        pretty = params['pretty']
        jsonp = params['jsonp']

        queries = {query: params[query] for query in recognized_arguments if params[query]}

        if not queries:
            return self.error(status_code=400, status_txt="MISSING_QUERY_ARGUMENTS")
        internal_callback = functools.partial(self._course_finish,
                pretty=pretty, jsonp=jsonp)
        self.course_pgquery.execute(queries, page=page, limit=limit,
                callback=internal_callback)

    def _match_associated_sections(self, courses, sections):
        # put the responses associated with the courses in the courses
        print 'COR', courses
        print 'SEC', sections
        for course, sections in zip(courses, sections):
            course['Sections'] = sections
        return courses

    def _course_finish(self, response, pretty=None, jsonp=None):
        if response:
            queries = []
            for course in response:
                queries.append({'course': course['Course']})
            internal_callback = functools.partial(self._section_finish,
                    courses=response, pretty=pretty, jsonp=jsonp)
            self.section_pgquery.execute_many(queries,
                    callback=internal_callback, unlimited=True)
        else:
            return self.error(status_code=204,
                    status_txt="NO_CONTENT_FOR_REQUEST", pretty=pretty,
                    jsonp=jsonp)

    def _section_finish(self, response, courses=None, pretty=None, jsonp=None):
        if response:
            response = self._match_associated_sections(courses, response)
            return self.api_response(response, pretty=pretty, jsonp=jsonp)
        else:
            return self.error(status_code=204,
                    status_txt="NO_CONTENT_FOR_REQUEST", pretty=pretty,
                    jsonp=jsonp)

class SectionsV2Handler(basic.BaseHandler):
    pgquery = lib.pg.PGQuery(sections, sections_functions)

    config = {
        'GET': {
            'params': basic.pg_function_params(sections_functions, {
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
    @basic.format_api_errors
    @basic.validate_token
    def process_get(self, params):
        recognized_arguments = self.valid_query_arguments(sections_functions)

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
