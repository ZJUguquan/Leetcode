# def chained(functions):
#     if len(functions) == 0:
#         return None
#     if len(functions) == 1:
#         return functions.pop(0)
#     result = functions.pop(0)

#     return lambda x: chained(functions[:])(result(x))
from functools import reduce
def chained(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)


def f1(x):
    return x * 2


def f2(x):
    return x + 2


def f3(x):
    return x ** 2


def f4(x):
    return x.split()


def f5(xs):
    return [x[::-1].title() for x in xs]


def f6(xs):
    return "_".join(xs)


s = 'shang yi xia shang'
s = 'lorem ipsum dolor'
print(chained([f4, f5, f6])(s))
