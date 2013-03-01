import app.basic

import models.affairs.affairs_functions as affairs
import models.athletics.athletics_functions as athletics
import models.courses.courses_functions as courses
import models.dining.dining_functions as dining
import models.housing.room_functions as room
import models.housing.building_functions as building
import models.uem.uem_functions as uem

from lib.docs import convert as c
from inspect import getmembers as mem
from inspect import isfunction as func

class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.redirect("docs/Documentation")

class DocsHandler(app.basic.BaseHandler):
    pages = {
            "affairs" : {
                "lead" : None,
                "endpoints" : {
                    "affairs/social_media" : {
                            "request": None,
                            "response": None,
                            "queries" : None,
                    },
                    "affairs/student_events" : {
                            "request": None,
                            "response": None,
                            "queries" : None,
                    },
                    "affairs/alumni_events" : {
                            "request": None,
                            "response": None,
                            "queries" : None,
                    },

                },
            },
            "athletics" : {
                "lead" : None,
                "endpoints" : {
                    "athletics" : {
                        "request": None,
                        "response": None,
                        "queries" : c(mem(athletics, func)),
                    },
                },
            },
            "courses" : {
                "lead" : None,
                "endpoints" : {
                    "courses" : {
                        "request" : None,
                        "response" : None,
                        "queries" : c(mem(courses, func)),
                    },
                },
            },
            "dining" : {
                "lead" : None,
                "endpoints" :{
                    "dining" : {
                        "request" : "Request",
                        "response" : "Response",
                        "queries" : c(mem(dining, func)),
                    },
                },
            },
            "housing" : {
                "lead" : None,
                "endpoints" : {
                    "housing/room" : {
                        "request" : None,
                        "response" : None,
                        "queries" : c(mem(room, func)),
                    },
                    "housing/building" : {
                        "request" : None,
                        "response" : None,
                        "queries" : c(mem(building, func)),
                },
            },
            "uem" : {
                "lead" : None,
                "endpoints" : {
                    "uem" : {
                        "request" : None,
                        "response" : None,
                        "queries" : c(mem(uem, func)),
                    },
                },
            },
        },
    }
    main = {
         "Authentication" : {
                "lead" : None,
                "endpoints" : None,
            },

            "Documentation"  : {
                "lead" : "Hello World",
                "endpoints" : None,
            },
    }

    def get(self, *arg):
        user = None
        current = arg[0]
        pages = self.pages
        if current not in self.pages and current not in self.main:
            current = "Documentation"
            page = self.main[current]
        elif current in self.main:
            current = arg[0]
            page = self.main[current]
        else:
            page = self.pages[current]


        print page["endpoints"]
        self.render('temp.html',
                pages=pages,
                current=current,
                lead=page["lead"],
                endpoints=page["endpoints"],
                user=user,)
