from app import basic
import tornado.web
import lib.pg
import functools

from models.courses_v2 import courses
from models.courses_v2 import courses_functions
from models.courses_v2 import sections
from models.courses_v2 import sections_functions

class CoursesV2Handler(basic.BaseHandler):
    course_pgquery = lib.pg.PGQuery(courses, courses_functions)
    section_pgquery = lib.pg.PGQuery(sections, sections_functions)

    @tornado.web.asynchronous
    @basic.format_api_errors
    @basic.validate_token
    def get(self):
        recognized_arguments = self.valid_query_arguments(courses_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", 0)
        page = self.get_int_argument("page", 0)
        pretty = self.get_bool_argument("pretty", None)
        jsonp = self.get_argument("jsonp", None)
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
                    callback=internal_callback)
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

    @tornado.web.asynchronous
    @basic.format_api_errors
    @basic.validate_token
    def get(self):
        recognized_arguments = self.valid_query_arguments(sections_functions)
        queries = self.get_recognized_arguments(recognized_arguments)
        limit = self.get_int_argument("limit", 0)
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
