# -*- coding: utf-8 -*-

from v_pre_handler import BaseHandler

try:
    from vmts_pre_define import pre_init
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Python environment had not be initialized.')


class LoginHandler(BaseHandler):

    def get(self):
        pass


class IndexHandler(BaseHandler):

    def get(self):

        pass
