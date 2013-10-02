import tornado.httpclient as http
import json
from urlparse import urljoin
from urllib import urlencode
import functools
import os

def es_async():
    index = os.getenv('ES_INDEX')
    if index is None:
        raise Exception('ES_INDEX variable missing')
    host = os.getenv('ES_HOST', 'localhost')
    port = int(os.getenv('ES_PORT', '9200'))
    return ElasticSearchClient(index, host, port)

class ElasticSearchClient(object):
    def __init__(self, index, host = 'localhost', port = 9200):
        self.base_url = 'http://' + host + ':' + str(port) + '/' + index + '/'
        self.http_client = http.AsyncHTTPClient()

    def index(self, dtype, docid, document, callback = None):
        internal_callback = functools.partial(self._wrap_callback,
                callback = callback)
        url = self.base_url + dtype + '/' + docid
        self.http_client.fetch(url, internal_callback,
                method = 'PUT', body = json.dumps(document))

    def get(self, dtype, docid, callback = None):
        internal_callback = functools.partial(self._wrap_callback,
                callback = callback)
        url = self.base_url + dtype + '/' + docid
        self.http_client.fetch(url, internal_callback)

    def delete(self, dtype, docid, callback = None):
        internal_callback = functools.partial(self._wrap_callback,
                callback = callback)
        url = self.base_url + dtype + '/' + docid
        self.http_client.fetch(url, internal_callback,
                method = 'DELETE')

    def search(self, dtype, query, callback = None):
        internal_callback = functools.partial(self._wrap_callback,
                callback = callback)
        url = self.base_url + dtype + '/_search?' + urlencode({'q': query})
        self.http_client.fetch(url, internal_callback)

    def _wrap_callback(self, response, callback):
        if callback is None:
            return
        response.rethrow()
        callback(json.loads(response.body))
