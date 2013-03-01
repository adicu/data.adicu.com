import app.basic


class MainHandler(app.basic.BaseHandler):
    def get(self):
        self.redirect("docs")

class DocsHandler(app.basic.BaseHandler):
    pages = {
            # "Documentation" : {
                    # "lead" : "Welcome to the API Data Documentation",
                    # "endpoints" : None,
            # },
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
                        "queries" : None,
                    },
                },
            },
            "courses" : {
                "lead" : None,
                "endpoints" : {
                    "courses" : {
                        "request" : None,
                        "response" : None,
                        "queries" : None,
                    },
                },
            },
            "dining" : {
                "lead" : None,
                "endpoints" :{
                    "dining" : {
                        "request" : None,
                        "response" : None,
                        "queries" : None,
                    },
                },
            },
            "housing" : {
                "lead" : None,
                "endpoints" : {
                    "housing/room" : {
                        "request" : None,
                        "response" : None,
                        "queries" : None,
                    },
                    "housing/building" : {
                        "request" : None,
                        "response" : None,
                        "queries" : None,
                },
            },
            "uem" : {
                "lead" : None,
                "endpoints" : {
                    "uem" : {
                        "request" : None,
                        "response" : None,
                        "queries" : None,
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
            }
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


        self.render('temp.html',
                pages=pages,
                current=current,
                lead=page["lead"],
                endpoints=page["endpoints"],
                user=user,)
