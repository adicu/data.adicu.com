import tornado.web
import hashlib
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

class ProfileHandler(app.basic.BaseHandler):
    def get(self):
        if self.get_secure_cookie("user"):
            self.write(self.get_secure_cookie("_id"))
        else:
            self.write("You are not auth'd")

class DocsHandler(app.basic.BaseHandler):
    pages = {
            "affairs" : {
                "lead" : """The affairs endpoint is pretty different from the
                others, as this one doesn't have any query parameters, just
                ping the endpoint, and see all the results we have fly!""",
                "endpoints" : {
                    "affairs/social_media" : {
                            "request": "http://data.adicu.com/affairs/social_media?pretty=true&api_token=TOKEN",
                            "response": """{
    "status_code": 200,
    "data": [
        {
            "Facebook": "http://www.facebook.com/ColumbiaCSA",
            "social_media": true,
            "Name / Lead Office": "Center for Student Advising",
            "Twitter Handle": "http://twitter.com/ColumbiaCSA"
        },""",
                            "queries" : None,
                    },
                    "affairs/student_events" : {
                        "request": "http://data.adicu.com/affairs/student_events?pretty=true&api_token=TOKEN",
                            "response": """{
    "status_code": 200,
    "data": [
        {
            "": "",
            "student_events": true,
            "Description": "Reps from Tufts Vet School will present on veterinary medicine",
            "Lead Office": "PreProfessional Advising (CSA)",
            "Audience": "All students interested in veterinary medicine",
            "Location": "401 Lerner",
            "Time": "6:00 - 7:30 p.m.",
            "Date": "2013-02-25 00:00:00",
            "Event": "Tufts School of Vet Medicine Visit"
        },""",
                            "queries" : None,
                    },
                    "affairs/alumni_events" : {
                            "request": "http://data.adicu.com/affairs/alumni_events?pretty=true&api_token=TOKEN",
                            "response": """{
    "status_code": 200,
    "data": [
        {
            "STATUS": "Confirmed",
            "LEAD ALUMNI AFFAIRS STAFF": "Trimmer*",
            "SPEAKER/PURPOSE": "Board Meeting",
            "EVENT TIME": "7 p.m.",
            "Sponsor": "CCYA",
            "VENUE/LOCATION": "CAC, Schapiro Conference Room",
            "DATE": "2013-02-20 00:00:00",
            "TARGET AUDIENCE": "CCYA Board Members",
            "EVENT": "CCYA Full Board Meeting",
            "alumni_events": true
        },""",
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
                        "request": "http://data.adicu.com/athletics?win=true&pretty=true&api_token=TOKEN",
                        "response": """ {
    "status_code": 200,
    "data": [
        {
            "feed": "results",
            "sport": "wrestling",
            "title": "Wrestling: vs San Francisco State (01/06/2013) - W (28-8)",
            "win": true,
            "article_link": "http://www.gocolumbialions.com/ViewArticle.dbml?DB_OEM_ID=9600&amp;ATCLID=205878762",
            "score": "28-8",
            "link": "http://www.gocolumbialions.com//SportSelect.dbml?DB_OEM_ID=9600&SPID=3876&SPSID=43591&Q_SEASON=2012",
            "location": "San Luis Obispo, Calif.",
            "time": "2013-01-06 15:00:00",
            "opponent": "San Francisco State"
        },""",
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
                        "request" : "http://data.adicu.com/courses?building=pupin&limit=1&pretty=true&api_token=API_TOKEN",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "CampusCode": "MORN",
            "CampusName": "MORNINGSIDE",
            "StartTime2": "None",
            "StartTime1": "15:00:00",
            "CourseTitle": "EARTH, MOON AND PLANETS",
            "MinUnits": 0,
            "CallNumber": "66696",
            "Term": "20122",
            "EndTime1": "17:10:00",
            "Instructor1Name": "APPLEGATE, JAMES H",
            "Building1": "PUPIN LABORA",
            "Building2": null,
            "NumEnrolled": 3,
            "SchoolName": "SCHOOL OF CONTINUING EDUCATION",
            "DepartmentName": "ASTRONOMY",
            "MeetsOn1": "TR",
            "MaxSize": 999,
            "EndTime2": "None",
            "MeetsOn2": null,
            "TypeName": "LECTURE",
            "NumFixedUnits": 30,
            "MaxUnits": 0,
            "Room2": null,
            "Room1": "1332",
            "Approval": "",
            "CourseSubtitle": "EARTH, MOON AND PLANETS"
        }
    ],
    "status_txt": "OK"
} """,
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
                        "request" : "http://data.adicu.com/dining?menu_item=pizza&pretty=true&api_token=TOKEN",
                        "response" : """ {
    "status_code": 200,
    "data": [
        {
            "url": "http://dining.columbia.edu/122week-one-tuesday-lunch-fbc",
            "menu": [
                "Firecracker Chicken Wrap",
                "Cheese Pizza",
                "Pepperoni Pizza",
                "Genovese Pizza",
                "Mushroom & Garlic Pizza",
                "Meatball Hero",
                "Chicken Tortilla Soup",
                "Smoked Ham Calzone",
                "Broccoli & Cheddar Soup",
                "Grits",
                "Waffles"
            ],
            "place": "Fer",
            "day": "2013-01-22 00:00:00",
            "meal_type": "LU"
        },""",
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
                    "housing/rooms" : {
                        "request" : "http://data.adicu.com/housing/rooms?shared_bathroom=true&api_token=TOKEN",
                        "response" : "",
                        "queries" : c(mem(room, func)),
                    },
                    "housing/buildings" : {
                        "request" : "http://data.adicu.com/housing/buildings?name=&api_token=TOKEN",
                        "response" : "",
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
                        "request" : "http://data.adicu.com/uem?room=wien&pretty=true&api_token=API_TOKEN",
                        "response" : """{
    "status_code": 200,
    "data": [
        {
            "Event Name": "Varsity Show - Rehearsal",
            "End": "2013-02-28 23:00:00",
            "Room": "Wien Lounge",
            "Start": "2013-02-28 20:00:00",
            "Date": "2013-02-28 00:00:00",
            "id": "51302459c749140b2a2dc49b"
        },
    "status_txt": "OK",
    }""",
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
        user = {}
        if not self.get_secure_cookie("name"):
            user["name"] = self.get_secure_cookie("name")
            user["photo_url"] = hashlib.md5(self.get_secure_cookie("email")).hexdigest()
            user["token"] = self.get_secure_cookie("_id")
        else:
            user = None
        print user
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
