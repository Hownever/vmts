# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpclient

from apps.auto_test.libs.envelope import soap_request

class SingleQueryHandler(tornado.web.RequestHandler):

    def get(self):
        return 'usage: blablablabla'

    def post(self):
        '''
        recv post msg, params:
         "url","method", "params"
        '''
        self.url = self.get_argument('url')
        self.method = self.get_argument('method')
        try:
            self.params = self.get_argument('params')
            (head, data) = soap_request(self.url, self.method, self.params)
        except tornado.web.MissingArgumentError:
            (head, data) = soap_request(self.url, self.method)

        client = tornado.httpclient.HTTPClient()
        self.response = client.fetch(self.url, data, method='POST')
        return self.response