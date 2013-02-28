import tornado.web
import tornado.httpclient

import functools
import logging
import simplejson as json
import urllib
import lib.pg
import lib.auth as auth

from lib.ArgumentMixin import ArgumentMixin

class BaseHandler(tornado.web.RequestHandler, ArgumentMixin):
    http = tornado.httpclient.AsyncHTTPClient()

    token_auth = auth.TokenAuth()
    
    @property
    def pg(self):
        if not hasattr(self.application, 'pg'):
            self.application.pg = lib.pg.pg_aync()
        return self.application.pg

    def api_call(self, url, params, callback, connect_timeout=10, request_timeout=10, headers=None, user_agent=None):
        """start an async GET api call"""
        headers = headers or {}
        if params:
            uri = url + '?' + urllib.urlencode(params, doseq=1)
        else:
            uri = url
        req = tornado.httpclient.HTTPRequest(url=uri, \
                        method='GET',
                        headers = headers or {},
                        follow_redirects=False,
                        connect_timeout=connect_timeout,
                        request_timeout=request_timeout,
                        user_agent=user_agent)
        self.http.fetch(req, callback=functools.partial(self._finish_http_fetch, callback=callback))

    def _finish_http_fetch(self, response, callback):
        logging.debug("finished %d %s %s %0.2fms", response.code, response.request.method, response.request.url, response.request_time * 1000)
        callback(response)

    def post(self, *args, **kwargs):
        # this should be overridden when a post is actually handled
        return self.error(405, 'HTTP_GET_REQUIRED')
    
    def error(self, status_code, status_txt, data=None):
        """write an api error in the appropriate response format"""
        self.api_response(status_code=status_code, status_txt=status_txt, data=data)

    def api_response(self, data, status_code=200, status_txt="OK", pretty=None):
        """write an api response in json"""
        self.set_header("Content-Type", "application/json; charset=utf-8")
        if pretty:
            pretty = 4 * ' '
        print pretty
        self.finish(json.dumps(dict(data=data, status_code=status_code,
            status_txt=status_txt), indent=pretty))

    def get_recognized_arguments(self, accepted_queries):
        queries = {query: self.get_argument(query)
                for query in accepted_queries if self.get_argument(query, None)}
        return queries
    
    # We define a valid query parameter if we have a function for it model_functions
    def valid_query_arguments(self, model_functions):
        return [func for func in dir(model_functions) if not "__" in func]

    def finish_validate_token(self, valid=None, method=None, args=None, kwargs=None):
        if valid:
            return method(self, *args, **kwargs)
        else:
            return self.error(status_code=500, status_txt="INVALID_API_TOKEN")

def format_api_errors(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except tornado.web.HTTPError, e:
            logging.info(e)
            if e.log_message and e.log_message.startswith("Missing argument "):
                return self.error(status_code=e.status_code, status_txt='MISSING_ARG_%s' % (e.log_message.split()[-1].upper()))
            if e.log_message and e.log_message.startswith("Invalid argument "):
                return self.error(status_code=e.status_code, status_txt='INVALID_ARG_%s' % (e.log_message.split()[-1].upper()))
            return self.error(status_code=e.status_code, status_txt=e.log_message or 'UNKNOWN_ERROR')
        except:
            logging.exception('UNKNOWN API ERROR')
            return self.error(status_code=500, status_txt='UNKNOWN_ERROR')
    return wrapper

def validate_token(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        api_token = self.get_argument('api_token', None)
        internal_callback = functools.partial(self.finish_validate_token, method=method, args=args, kwargs=kwargs)
        self.token_auth.validate_token(api_token, callback=internal_callback)
    return wrapper

