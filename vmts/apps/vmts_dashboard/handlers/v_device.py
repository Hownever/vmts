# -*- coding: utf-8 -*-

from v_pre_handler import BaseHandler

try:
    from vmts_pre_define import pre_init
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Python environment had not be initialized.')


class DeviceInfo(BaseHandler):

    def get(self):

        # todo: return device info
        pass

    def post(self):

        # todo: create new device info
        pass

    def put(self):

        # todo: update device info
        pass

    def delete(self):

        # todo: delete device info
        pass


class TaskInfo(BaseHandler):

    def get(self):

        # todo: return task info
        pass

    def post(self):

        # todo: creat new task info
        pass

    def put(self):

        # todo: update task info
        pass

    def delete(self):

        # todo: delete task info
        pass