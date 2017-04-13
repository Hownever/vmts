# -*- coding: utf-8 -*-

from pre_handler import BaseHandler

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Python environment had not be initialized.')


class UserInfo(BaseHandler):

    def get(self):

        # todo: return user info
        pass

    def post(self):

        # todo: create new user info
        pass

    def put(self):

        # todo: update user info
        pass

    def delete(self):

        # todo: delete user info
        pass