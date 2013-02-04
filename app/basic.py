import tornado.web
import tornado.httpclient

import functools
import logging
import simplejson as json
import urllib

from lib.ArgumentMixin import ArgumentMixin
import settings

class BaseHandler(tornado.web.RequestHandler, ArgumentMixin):
    http = tornado.httpclient.AsyncHTTPClient()

    def get_render_args(self):
        return {
            'host' : self.host,
            'uri' : self.request.uri,
            # values or functions that should get passed to every render() call
            # 'site_wide_message' : lib.site_wide_message.get(),
        }
    
    def render(self, *args, **kwargs):
        """ pass in extra values to templates """
        new_kwargs = self.get_render_args()
        new_kwargs.update(kwargs)
        self.set_header("Cache-Control", "no-cache, no-store, max-age=0, must-revalidate")
        self.set_header("Pragma", "no-cache")
        # turn on google chrome frame when available
        if 'chromeframe' in self.request.headers.get('User-Agent', []):
            self.set_header("X-UA-Compatible","chrome=1")
        return super(BaseHandler, self).render(*args, **new_kwargs)

    def get_current_user(self):
        return self.get_secure_cookie('user')
    
    @property
    def host(self):
        return self.request.host.split(':', 1)[0].lower()
    
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
                        user_agent=user_agent or 'bitlybot')
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

    def api_response(self, data, status_code=200, status_txt="OK"):
        """write an api response in json"""
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.finish(json.dumps(dict(data=data, status_code=status_code, status_txt=status_txt)))

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
