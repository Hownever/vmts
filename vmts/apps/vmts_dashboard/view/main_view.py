# -*- coding: utf-8 -*-

import tornado.gen
from tornado.web import RequestHandler


try:
    from vmts_pre_define import pre_init
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Python environment had not be initialized.')


class BaseHandler(RequestHandler):

    # todo: basic handler.
    pass


class SessionValidationHandler(RequestHandler):

    @tornado.gen.coroutine
    def check_current_user(self):

        yield

class LoginHandler():

    def get(self):
