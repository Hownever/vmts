# -*- coding: utf-8 -*-

import tornado.gen
from pre_handler import BaseHandler

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except:
    raise ImportError('Vmts environment had not be initialized.')


class DeviceInfo(BaseHandler):

    @tornado.gen.coroutine
    def get(self, dev):

        # todo: return device info
        pass

    def post(self, dev):

        # todo: create new device info
        pass

    def put(self, dev):

        # todo: update device info
        pass

    def delete(self, dev):

        # todo: delete device info
        pass
