#-*- coding: utf-8 -*-

from vmts_exceptions import FieldValidationError

def create_table(instance, ):
    pass

class Attribute(object):

    def __init__(self,
                 name,
                 required=False,
                 unique=False,
                 default=None,
                 **additions):
        try:
            self.f_type = additions['f_type']
            self.primary = additions['primary']
            self.unsigned = additions['unsigned']
            self.binary = additions['binary']
            self.zerofill = additions['zerofill']
            self.autoincr = additions['autoincr']
            self.db_type = 'mysql'
        except KeyError:
            self.db_type = 'redis'

        self.name = name
        self.required = required
        self.unique = unique
        self.default = default



    def __get__(self, instance, owner):
        try:
            return getattr(instance, '_' + self.name)
        except AttributeError:
            pass

    def __set__(self, instance, value):
        setattr(instance, '_' + self.name, value)

    def typecast_for_read(self, value):
        return value.decode('utf-8')

    def typecast_for_storage(self, value):
        try:
            return unicode(value)
        except UnicodeError:
            return value.decode('utf-8')

    def value_type(self):
        return unicode

    def acceptable_types(self):
        return basestring

    def validate(self, instance):
        val = getattr(instance, self.name)
        errors= []
        if val and not isinstance(val, self.acceptable_types()):
            errors.append((self.name, 'Bad Type'))

        if self.required:
            if val is None or not unicode(val).strip():
                errors.append((self.name, 'required'))

        if val and self.unique:
            err = self.validate_uniqueness(instance, val)
            if err:
                errors.append(err)

        if self.validator:
            r = self.validator(self.name, val)
            if r:
                errors.extend(r)

        if errors:
            raise FieldValidationError(errors)

    def validate_uniqueness(self, instance, val):
        encoded = self.typecast_for_storage(val)
        same = len()


class IntField(Attribute):

    def __init__(self, *args, **kw):
        super(IntField, self).__init__(*args, **kw)




class FloatField(Attribute):

    def __init__(self):


class ModelBase(type):

    def __init__(cls, name, bases, attrs):
        super(ModelBase, cls).__init__(name, bases, attrs)


class Model(object):
    __metaclass__ = ModelBase

    def __init__(self):
        pass

