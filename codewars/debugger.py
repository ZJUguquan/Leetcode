import datetime
from functools import wraps


class Debugger(object):
    attribute_acceses = []
    method_calls = []


class Meta(type):
    def __new__(cls, cls_name, bases, cls_dict):
        def meassure(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = datetime.datetime.now()
                ret = func(*args, **kwargs)
                end = datetime.datetime.now()
                Debugger.method_calls.append({
                    'class': type(args[0]),
                    'method': str(func),
                    'args': args,
                    'kwargs': kwargs,
                    'time': (end - start),
                })
                return ret
            return wrapper

        def getter(self, key):
            Debugger.attribute_acceses.append({
                'action': 'get',
                'class': type(self),
                'attribute': key
            })
            return object.__getattribute__(self, key)

        def setter(self, key, value):
            Debugger.attribute_acceses.append({
                'action': 'set',
                'class': type(self),
                'attribute': key,
                'value': value
            })
            object.__setattr__(self, key, value)

        for name, item in cls_dict.items():
            if callable(item):
                cls_dict[name] = meassure(item)

        cls_dict['__getattribute__'] = getter
        cls_dict['__setattr__'] = setter

        return super(Meta, cls).__new__(cls, cls_name, bases, cls_dict)