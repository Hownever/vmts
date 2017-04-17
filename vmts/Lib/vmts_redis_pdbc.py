# -*- coding: utf-8 -*-

import redis

from vmts_exceptions import DefaultConnectionPoolInitializationError
from vmts_pre_define import cfg

redis_conf = cfg.get_module('vmts_conf').redis


def singleton(cls):
    """
    Singleton decorator function.
    :param cls: Class object decorated.
    :return: wrap decorated object, and return its self.
    """

    instances = {}

    def _singleton(db, **kw):
        if cls not in instances and db not in instances[cls]:
            instances[cls] = {db: cls(db, **kw)}
        return instances[cls]
    return _singleton


@singleton
class DefaultConnectionPool(redis.ConnectionPool):
    """
    Custom redis connection-pool, only provide several parameters for the specific requirement.
    """

    def __init__(self, db, **kw):

        super(DefaultConnectionPool, self).__init__(host=kw['host'], port=kw['port'], password=kw['password'], db=db)


class Redis(redis.StrictRedis):
    """
    Custom redis connection class, suitable for custom requirement.
    """

    def __init__(self, db):

        try:
            pool = DefaultConnectionPool(db, host=redis_conf.host, port=redis_conf.port, password=redis_conf.password)
        except:
            raise DefaultConnectionPoolInitializationError

        super(Redis, self).__init__(connection_pool=pool)
