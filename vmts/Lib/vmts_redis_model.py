#-*- coding: utf-8 -*-


class ModelBase(type):

    pass


class Model(object):
    __metaclass__ = ModelBase

    def