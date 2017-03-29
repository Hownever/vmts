# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
    from vmts_exceptions import *
except ImportError:
    raise ImportError('Python environment had not be initialized.')

def main():
    settings = cfg.get_module('vmts_conf')