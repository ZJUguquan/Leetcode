class ValidationError(Exception):
    def __init__(self, attribute_name, msg):
        self.attribute_name = attribute_name
        self.msg = msg

    def __str__(self):
        return 'Attribute `%s`: %s.' % (self.attribute_name, self.msg)


class CharField(object):
    def __init__(self, max_length=None):
        self.max_length = max_length


class IntegerField(object):
    def __init__(self, min_value=None, max_value=None, blank=True):
        self.min_value = min_value
        self.max_value = max_value
        self.blank = blank


class BooleanField(object):
    def __init__(s)


class DateTimeField(object):
    pass


class EmailField(object):
    pass


class ModelMeta(type):
    pass


class Model(object):
    __metaclass__ = ModelMeta
