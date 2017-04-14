# -*- coding: utf-8 -*-

from pre_handler import BaseHandler

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Vmts environment had not be initialized.')


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
