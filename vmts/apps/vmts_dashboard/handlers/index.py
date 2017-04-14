# -*- coding: utf-8 -*-

from pre_handler import BaseHandler


try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Vmts environment had not be initialized.')


class LoginHandler(BaseHandler):

    def get(self):

        pass


class LogoutHandler(BaseHandler):

    def get(self):

        self.render("login.html")

    def post(self):

        user = self.get_argument("user")
        pwd = self.get_argument("password")




class IndexHandler(BaseHandler):

    def get(self):

        pass
