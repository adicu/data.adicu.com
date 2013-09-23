import app.basic
import tornado.web
import functools
import collections
import hashlib
import json

import docs.authentication
import docs.documentation
import docs.courses
import docs.courses_v2
import docs.housing

class DocsHandler(app.basic.BaseHandler):
    pages = {
                "Documentation"  : docs.documentation,
                "Authentication" : docs.authentication,
                "courses"        : docs.courses,
                "courses (v2)"   : docs.courses_v2,
                "housing"        : docs.housing,
            }

    def get(self, *arg):
        userstr = self.get_secure_cookie("user")
        if userstr:
            user = json.loads(userstr)
            email_hash = hashlib.md5(user['email']).hexdigest()
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
