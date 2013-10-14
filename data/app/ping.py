from app import basic
import app
import functools

import json

class PingHandler(basic.BaseHandler):
    def process_get(self, params):
        self.write('Pong')
        self.write(json.dumps(params))
        self.finish('OK')

    def process_head(self, params):
        self.write(json.dumps(params))
        self.finish('OK')

    config = {
        'GET': {
            'params': {
                'token': {
                    'type': 'string',
                    'default': None
                    }
                },
            'function': 'process_get'
            },
        'HEAD': {
            'params': None,
            'function': 'process_head'
            }
        }
