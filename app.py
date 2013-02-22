import tornado.options
import tornado.httpserver
import tornado.ioloop

import logging
import os

import app.main

env = os.environ
class Application(tornado.web.Application):
    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)

        app_settings = {
            'debug': "dev",
            #"xsrf_cookies" : True,
            "cookie_secret" : 'app',
            "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
            "static_path" : os.path.join(os.path.dirname(__file__), "static"),
            "autoescape" : None,
        }

        handlers = [
            (r"/$", app.main.MainHandler),
            (r"/ping$", PingHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **app_settings)

class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('OK')
    def head(self):
        self.finish('OK')


if __name__ == "__main__":
    # this port should be unique system wide; all ports used should be listed in ~/services.py
    tornado.options.define("port", default=int(env["PORT"]), help="Listen on port", type=int)
    tornado.options.parse_command_line()
    logging.info("starting app on 0.0.0.0:%d" % tornado.options.options.port)
    http_server = tornado.httpserver.HTTPServer(request_callback=Application())
    http_server.listen(tornado.options.options.port, address="0.0.0.0")
    tornado.ioloop.IOLoop.instance().start()
