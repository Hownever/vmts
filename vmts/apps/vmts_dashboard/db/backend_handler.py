# -*- coding: utf-8 -*-

import tornado.httpclient

from vmts_jsonrpc_protocol import JsonRpcProtocolConstructor


def request():

    client = tornado.httpclient.AsyncHTTPClient()