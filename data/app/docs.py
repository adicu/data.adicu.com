import app.basic
import tornado.web
import lib.mongo
import functools
import inspect

import models.affairs.affairs_functions as affairs
import models.athletics.athletics_functions as athletics
import models.courses.courses_functions as courses
import models.dining.dining_functions as dining
import models.housing.room_functions as housing
#import models.uem.uem_functions as uem

class DocsHandler(app.basic.BaseHandler):
    accepted_pages_args = {
        "affairs"  : inspect.getmembers(affairs, inspect.isfunction),
        "athletics": inspect.getmembers(athletics, inspect.isfunction),
        "courses"  : inspect.getmembers(courses, inspect.isfunction),
        "dining"   : inspect.getmembers(dining, inspect.isfunction),
        "housing"  : inspect.getmembers(housing, inspect.isfunction),
#        "uem"      : inspect.getmembers(athletics, inspect.isfunction),
        }

    def get(self, *arg):
        if not arg:
            self.render('index.html', message="Welcome to docs")
        slug = arg[0]
        if slug not in self.accepted_pages_args:
            self.render('index.html', message="Welcome to docs")
        else:
            self.render('docs.html', endpoint=slug,
                    params=self.accepted_pages_args[slug])
