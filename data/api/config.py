from collections import OrderedDict

import app.courses
import app.ping
import app.courses_v2
import app.housing

config = OrderedDict([
    (r'/ping$', {
        'handler': app.ping.PingHandler,
        'config': app.ping.PingHandler.config
        }),
    (r'/courses$', {
        'handler': app.courses.CoursesHandler,
        'config': app.courses.CoursesHandler.config
        }),
    (r'/courses/v2/courses$', {
        'handler': app.courses_v2.CoursesV2Handler,
        'config': app.courses_v2.CoursesV2Handler.config
        }),
    (r'/courses/v2/sections$', {
        'handler': app.courses_v2.SectionsV2Handler,
        'config': app.courses_v2.CoursesV2Handler.config
        }),
    (r'/courses/v2/search$', {
        'handler': app.courses_v2.FullTextSearchHandler,
        'config': app.courses_v2.FullTextSearchHandler.config
        }),
    (r'/housing/rooms$', {
        'handler': app.housing.RoomHandler,
        'config': app.housing.RoomHandler.config
        }),
    (r'/housing/buildings$', {
        'handler': app.housing.BuildingHandler,
        'config': app.housing.BuildingHandler.config
        }),
])

def api_handlers():
    handlers = []
    for endpoint, apiconf in config.iteritems():
        handlers.append((endpoint, apiconf['handler']))
    return handlers

