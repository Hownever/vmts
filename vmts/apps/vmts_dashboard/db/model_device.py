# -*- coding: utf-8 -*-

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
    from vmts_backend_client import query
    from vmts_orm import Model
except:
    raise ImportError('Vmts environment had not be initialized.')


class DeviceInterface(Model):

