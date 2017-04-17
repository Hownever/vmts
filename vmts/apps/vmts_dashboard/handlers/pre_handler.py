# -*- coding: utf-8 -*-

import tornado.gen
from tornado.web import RequestHandler

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except:
    raise ImportError('Vmts environment had not be initialized.')

__all__ = ["BaseHandler"]


class PreHandler(RequestHandler):
    pass


class SessionValidationHandler(RequestHandler):

    @tornado.gen.coroutine
    def check_current_user(self):
        yield


class BaseHandler(PreHandler, SessionValidationHandler):
    # todo: basic handler.
    pass
