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
                "lead" : """The affairs endpoint is pretty different from the
                others, as this one doesn't have any query parameters, just
                ping the endpoint, and see all the results we have fly!""",
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
                "lead" : """The athletics endpoint is kind of broken down by
                feed -- results and schedules.  Play around with the different
                sports, as some can be pretty interesting! After you've pinged
                it a couple times you'll start to notice the differences in
                format between results, and schedules and how sports names are
                formatted""",
                "endpoints" : {
                    "athletics" : {
                        "request": None,
                        "response": None,
                        "queries" : c(mem(athletics, func)),
                    },
                },
            },
            "courses" : {
                "lead" : """This endpoint is hiding a whole bunch of data! Make
                sure you use the different query parameters effectively to see
                its all done behind.  Think of it as one giant sql table
                you're making requests against.""",
                "endpoints" : {
                    "courses" : {
                        "request" : None,
                        "response" : None,
                        "queries" : c(mem(courses, func)),
                    },
                },
            },
            "dining" : {
                "lead" : """Dining, the must have endpoint for anyone with a
                stomach on this campus! Check out the way locations are done,
                they are abbreviated in a strange way, like 'fer' for
                ferris.""",
                "endpoints" :{
                    "dining" : {
                        "request" : "Request",
                        "response" : "Response",
                        "queries" : c(mem(dining, func)),
                    },
                },
            },
            "housing" : {
                "lead" : """Housing is broken down into two different endpoints,
                rooms and buildings.  Rooms has a bunch of room data (gasp) as
                well as some lottery information... Buildings has a list of
                amentities... We don't offer joins across these two datasets,
                so get creative! ;)""",
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
                "lead" : """UEM, for University Events Management is a delayed
                live feed of whats coming out UEM. Updated nightly, this
                endpoint has all the confirmed booked space on campus that UEM
                handles, which is alot.  Be sure to play around with the event
                name query param, because its probably the richest one""",
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
                "lead" : """To use any of the API's you must have an api_token
                and appended to your string as api_token=TOKEN. To get a
                token, login on the upper right. We use google auth to make
                the auth request. Once signed in, visit the token page to see
                your token, and get coding!""",
                "endpoints" : None,
            },

            "Documentation"  : {
                "lead" : """Documentation for the set of Data API's provided by,
                and maintained by the Application Development Initative at
                Columbia University.  Visit the different endpoints, get your
                api token, and start coding. There is some exciting stuff
                around there! If you have any set backs, feel free to ping
                hack@adicu.com and we'll get back to you as quick as we can.
                Please keep in mind this is API version 0.0 and is pretty
                rough and the edges. Report bugs, and help us make it better
                at github.com/adicu/data.adicu.com""",
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
