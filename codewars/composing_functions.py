

import functools

def create_iterator(func, n):

    functions = list() for _ in range(n): functions.append(func)

    def compose2(f, g): return lambda x: f(g(x)) return
    functools.reduce(compose2, functions, lambda x: x)


def get_double(n):
    return 2*n

# double_iterator = create_iterator(get_double, 1)

# print(double_iterator(3) == 6)
# print(double_iterator(5) == 10)

get_quadruple = create_iterator(get_double, 2)

print(get_quadruple(2) )
print(get_quadruple(5) )
