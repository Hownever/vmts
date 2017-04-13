# -*- coding: utf-8 -*-


import time

from vmts_logger import VmtsLogger


def timer(func):
    """
    Time cost decorator, only for function.
    :param func: <function> object.
    :return: Decorator.
    """

    def _timer(*args, **kw):
        t0 = time.time()
        res = func(*args, **kw)
        t1 = time.time()

        VmtsLogger('timecost').info("{function} time cost: {res}".format(function=str(func), res=t1 - t0))

        return res
    return _timer
