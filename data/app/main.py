import app.basic

class MainHandler(app.basic.BaseHandler):
    params = [
            ("Documentation"),
            ("Authentication"),
            ("affairs/social_media"),
            ("affairs/student_events"),
            ("affairs/alumni_events"),
            ("athletics"),
            ("courses"),
            ("dining"),
            ("housing/room"),
            ("housing/building"),
            ("uem"),
        ]
    def get(self):
        self.render('temp.html',
                params=self.params,
                current="Documentation",
                queries = {"exampe":"example text"},
                user=None,)
