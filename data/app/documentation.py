import app.basic
import tornado.web
import lib.mongo
import functools
import collections
import hashlib

import docs.affairs
import docs.athletics
import docs.authentication
import docs.documentation
import docs.courses
import docs.courses_v2
import docs.dining
import docs.housing
import docs.uem


class DocsHandler(app.basic.BaseHandler):
    pages = {
                "Documentation"  : docs.documentation,
                "Authentication" : docs.authentication,
                "affairs"        : docs.affairs,
                "athletics"      : docs.athletics,
                "courses"        : docs.courses,
                "courses (v2)"   : docs.courses_v2,
                "dining"         : docs.dining,
                "housing"        : docs.housing,
                "uem"            : docs.uem,
            }

    def get(self, *arg):
        user = {}
        if self.get_secure_cookie("user"):
            user["token"] = self.get_secure_cookie("_id")
            user["name"] = self.get_secure_cookie("name")
            email_hash = hashlib.md5(self.get_secure_cookie("email")).hexdigest()
            user["photo"] = "https://secure.gravatar.com/avatar/%s?s=50" % email_hash
        else:
            user = None

        current = arg[0]
        pages = collections.OrderedDict(sorted(self.pages.items()))

        if current not in self.pages:
            current = "Documentation"

        lead = pages[current].get_lead()
        endpoints = pages[current].get_endpoints()

        self.render('docs.html',
                pages=pages,
                current=current,
                lead=lead,
                endpoints=endpoints,
                user=user
                )
