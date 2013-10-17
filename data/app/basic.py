import tornado.web
import tornado.httpclient
import tornado.escape
import tornado.auth

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

    def dispatch_func(self, method, *args, **kwargs):
        params = dict()
        jsonp = params.get('jsonp')
        pretty = params.get('pretty')

        if method in self.config:
            verb_conf = self.config[method]
            valid_params = verb_conf['params']

            if valid_params:
                for param in valid_params:
                    param_config = valid_params[param]
                    param_type = param_config['type']

                    try:
                        required = False
                        param_default = param_config['default']
                    except:
                        # parameter is required
                        required = True
                        param_default = None

                    if param_type == 'bool':
                        get_func = self.get_bool_argument
                    elif param_type == 'int':
                        get_func = self.get_int_argument
                    elif param_type == 'string':
                        get_func = self.get_argument
                    else:
                        raise 'Unrecognized param type'

                    if required:
                        value = get_func(param)
                    else:
                        value = get_func(param, param_default)

                    # store parameter
                    params[param] = value

            showhelp = self.get_bool_argument('help', None)

            if showhelp:
                return self.api_response(data=valid_params, jsonp=jsonp, pretty=pretty)

            func = getattr(self, verb_conf['function'])
            try:
                return func(params)
            except tornado.web.HTTPError as e:
                return self.error(400, str(e), jsonp=jsonp, pretty=pretty)
            except Exception as e:
                return self.error(500, 'We blew something up, sorry\n' + str(e),
                        jsonp=jsonp, pretty=pretty)
        else:
            return self.error(405, 'HTTP_%s_FORBIDDEN' % method,
                    jsonp=jsonp, pretty=pretty)

    def get(self, *args, **kwargs):
        return self.dispatch_func('GET', *args, **kwargs)

    def head(self, *args, **kwargs):
        return self.dispatch_func('HEAD', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.dispatch_func('POST', *args, **kwargs)
    
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

    def error(self, status_code, status_txt, data=None, jsonp=None, pretty=None):
        """write an api error in the appropriate response format"""
        self.api_response(status_code=status_code, status_txt=status_txt,
                data=data, jsonp=jsonp, pretty=pretty)

    def api_response(self, data, status_code=200, status_txt="OK",
            pretty=None, jsonp=None):
        """write an api response in json"""
        if pretty:
            pretty = 4 * ' '
        if jsonp:
            self.set_header("Content-Type", "application/javascript")
            self.finish(jsonp + "(" + json.dumps(dict(data=data, status_code=status_code,
                status_txt=status_txt)) + ")")
        else:
            self.set_header("Content-Type", "application/json; charset=utf-8")
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
            params = args[0]
            jsonp = params.get('jsonp')
            pretty = params.get('pretty')
            return self.error(status_code=401, status_txt="INVALID_API_TOKEN",
                    jsonp=jsonp, pretty=pretty)
    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if not user_json: return None
        return tornado.escape.json_decode(user_json)

def format_api_errors(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        params = args[0]
        jsonp = params.get('jsonp')
        pretty = params.get('pretty')
        try:
            return method(self, *args, **kwargs)
        except tornado.web.HTTPError, e:
            logging.info(e)
            if e.log_message and e.log_message.startswith("Missing argument "):
                return self.error(status_code=e.status_code,
                        status_txt='MISSING_ARG_%s' % (
                            e.log_message.split()[-1].upper()),
                        jsonp=jsonp, pretty=pretty)
            if e.log_message and e.log_message.startswith("Invalid argument "):
                return self.error(status_code=e.status_code,
                        status_txt='INVALID_ARG_%s' % (
                            e.log_message.split()[-1].upper()),
                        jsonp=jsonp, pretty=pretty)
            return self.error(status_code=e.status_code,
                    status_txt=e.log_message or 'UNKNOWN_ERROR',
                    jsonp=jsonp, pretty=pretty)
        except:
            logging.exception('UNKNOWN API ERROR')
            return self.error(status_code=500, status_txt='UNKNOWN_ERROR',
                    jsonp=jsonp, pretty=pretty)
    return wrapper

def validate_token(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        api_token = self.get_argument('api_token', None)
        internal_callback = functools.partial(self.finish_validate_token, method=method, args=args, kwargs=kwargs)
        self.token_auth.validate_token(api_token, callback=internal_callback)
    return wrapper

def pg_function_params(model_functions, other_params):
    return dict({
            func: {
                'type': 'string',
                'default': None
                }
                for func in dir(model_functions) if not "__" in func
            }, **other_params)
