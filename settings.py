import tornado.options
import functools

tornado.options.define("environment", default="dev", help="environment")

options = {
    # default settings that do not change per environment go here
    'asynchttp_max_simultaneous_connections' : 100, # number of connections held open by pycurl via tornado.httpclient.AsyncHTTPClient
    'asynchttp_max_clients' : 50, # number of concurrent tornado.httpclient.AsyncHTTPClient requests
}

def env():
    return tornado.options.options.environment

def get(option):
    return options[option]
