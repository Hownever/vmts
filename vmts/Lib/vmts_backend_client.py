# -*- coding: utf-8 -*-

import tornado.httpclient
import tornado.httputil

from vmts_pre_define import cfg
from vmts_exceptions import LackofHTTPHeadersError, RpcValidationError, UnmatchedUidError
from vmts_jsonrpc_protocol import JsonRpcProtocolConstructor

config = cfg.get_module('vmts_apps')


class BackendHTTPRequest(tornado.httpclient.HTTPRequest):
    """
    Custom http request object for backend query.
    """

    def __init__(self, url, method="GET", headers=None, body=None,
                 request_timeout=None, user_agent=config.backend.request_user_agent):
        if not isinstance(headers, tornado.httputil.HTTPHeaders):
            if type(headers) == dict:
                headers = tornado.httputil.HTTPHeaders(headers)
            else:
                raise LackofHTTPHeadersError

        super(BackendHTTPRequest, self).__init__(url=url, method=method, headers=headers,
                                                 body=body, request_timeout=request_timeout,
                                                 user_agent=user_agent)


def query(method, params, url, http_method='POST', headers=None, request_timeout=None):
    """
    Function for doing database query through rpc.
    :param method: method name of remote procedure call.
    :param params: params of remote procedure call.
    :param url: remote url string.
    :param http_method: http method, default POST.
    :param headers: http additional headers.
    :param request_timeout: entire http request time cost limit, default 20.
    :return: resolved response.
    """

    if type(params) != dict:
        raise RpcValidationError

    with JsonRpcProtocolConstructor('request') as jrpc:
        body = jrpc.pack(method, params)
        uid = jrpc.uid

    request = BackendHTTPRequest(url, method=http_method, body=body, headers=headers,
                                 request_timeout=request_timeout)

    client = tornado.httpclient.AsyncHTTPClient()
    res = client.fetch(url, request)

    with JsonRpcProtocolConstructor('response') as jrpc:
        rid, result, error = jrpc.unpack(res)
        if uid != rid:
            raise UnmatchedUidError

    return result, error
