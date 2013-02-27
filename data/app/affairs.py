import app.basic
import tornado.web
import lib.pg
import functools

import models.affairs.affairs as model
import models.affairs.affairs_functions as model_functions

class AffairsHandler(app.basic.BaseHandler):
    accepted_pages = ["social_media", "student_events", "alumni_events"]

    @tornado.web.asynchronous
    def get(self, *arg):
        limit = self.get_int_argument("limit", 0)
        page = self.get_int_argument("page", 0)
        pretty = self.get_bool_argument("pretty", None)
        if not (arg):
            # render template
            pass
        if arg not in self.accepted_pages:
            return self.error(status_code=404, status_txt="PAGE_NOT_FOUND")
        queries = {slug:True}
        if not (page or pretty or limit):
            # render template
            pass
        internal_callback = functools.partial(self._finish, pretty=pretty)
        self.mongo.execute(queries, page=page, limit=limit, callback=internal_callback)


    def _finish(self, response, pretty=None):
        if response:
            return self.api_response(response, pretty=pretty)
        else:
            return self.error(status_code=204, status_txt="NO_CONTENT_FOR_REQUEST")
