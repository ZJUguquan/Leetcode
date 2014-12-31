def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called += 1
        return fn(*args, **kwargs)
    wrapper.called = 0
    wrapper.__name__ = fn.__name__
    return wrapper


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


import sys


def count_calls(func, *args, **kwargs):
    calls = [-1]

    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer
    sys.settrace(tracer)
    rv = func(*args, **kwargs)
    return calls[0], rv

print(count_calls(add, 8, 12))
print(count_calls(misc_fun))
# print(dir(misc_fun))

# print(misc_fun.__call__)
