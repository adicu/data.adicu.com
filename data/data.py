import tornado.options
import tornado.httpserver
import tornado.ioloop

import logging
import os

import app.main
import app.courses
import app.courses_v2
import app.affairs
import app.dining
import app.athletics
import app.housing
import app.uem
import app.auth
import app.documentation


class Application(tornado.web.Application):
    def __init__(self, debug=False):
        logging.getLogger().setLevel(logging.DEBUG)

        app_settings = {
            "debug": debug,
            "xsrf_cookies" : False,
            "cookie_secret" : "32oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
            "static_path" : os.path.join(os.path.dirname(__file__), "static"),
            "autoescape" : None,
            "login_url" : "http://data.adicu.com/login",
        }

        handlers = [
            (r"/$", app.main.MainHandler),
            (r"/ping$", PingHandler),
            (r"/courses$", app.courses.CoursesHandler),
            (r"/courses/v2/courses$", app.courses_v2.CoursesV2Handler),
            (r"/courses/v2/sections$", app.courses_v2.SectionsV2Handler),
            (r"/dining$", app.dining.DiningHandler),
            (r"/uem$", app.uem.UemHandler),
            (r"/affairs$", app.affairs.AffairsHandler),
            (r"/affairs/([^/]+)", app.affairs.AffairsHandler),
            (r"/athletics$", app.athletics.athleticsHandler),
            (r"/housing/rooms$", app.housing.RoomHandler),
            (r"/housing/buildings$", app.housing.BuildingHandler),
            (r"/docs$", app.main.MainHandler),
            (r"/docs/([^/]+)", app.documentation.DocsHandler),
            (r"/login$", app.auth.LoginHandler),
            (r"/logout$", app.auth.LogoutHandler),
            (r"/profile$", app.main.ProfileHandler),

        ]
        debug = True
        tornado.web.Application.__init__(self, handlers, **app_settings)

class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('OK')
    def head(self):
        self.finish('OK')


if __name__ == "__main__":
    # this port should be unique system wide; all ports used should be listed in ~/services.py
    tornado.options.define("port", default=int(os.environ.get("PORT", "8080")), 
                            help="Port to listen on", type=int)
    tornado.options.define("debug", default=bool(os.environ.get("DEBUG")), 
                            help="Put app in debug mode", type=bool)
    tornado.options.parse_command_line()
    logging.info("starting app on 127.0.0.1:%d" % tornado.options.options.port)
    application = Application(debug=tornado.options.options.debug)
    http_server = tornado.httpserver.HTTPServer(request_callback=application)
    http_server.listen(tornado.options.options.port, address="127.0.0.1")
    tornado.ioloop.IOLoop.instance().start()
