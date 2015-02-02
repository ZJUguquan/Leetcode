# -*- coding: utf-8 -*-

# chained([a,b,c,d])(input)
# d(c(b(a(input))))
# def chained(functions):


def chained(functions):
    if len(functions) == 0:
        return None
    if len(functions) == 1:
        return functions.pop(0)
    result = functions.pop(0)
    return lambda x: chained(functions[:])(result(x))


def add(x):
    __str__ = 'add'
    return x + 2


def multi(x):
    __str__ = 'multi'
    return x * 2


def div(x):
    return x // 3


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


# test.assert_equals( chained([f1,f2,f3])(0), 4 )
# test.assert_equals( chained([f1,f2,f3])(2), 36 )
# test.assert_equals( chained([f3,f2,f1])(2), 12 )


com = chained([add, multi, div])
print(com(10))
print(chained([f1, f2, f3])(0))
print(chained([f1, f2, f3])(2))
print(chained([f3, f2, f1])(2))

m = ['0', ' ', 'c', ' ', 'o', ' ', 'f', ' ', 'i', ' ', '8', ' ', 'j', ' ', 'j', ' ', 's', ' ', 'q', ' ', 'f', ' ', '2', ' ', '3', ' ', 'q', ' ', 'k', ' ', 'g',
     ' ', 'a', ' ', '4', ' ', '1', ' ', 'g', ' ', '1', ' ', '1', ' ', 'e', ' ', 'i', ' ', 'd', ' ', 'd', ' ', '9', ' ', 'g', ' ', '0', ' ', 'x', ' ', 'g', ' ', 'b']
m2 = ['0', ' ', 'C', ' ', 'O', ' ', 'F', ' ', 'I', ' ', '8', ' ', 'J', ' ', 'J', ' ', 'S', ' ', 'Q', ' ', 'F', ' ', '2', ' ', '3', ' ', 'Q', ' ', 'K', ' ', 'G',
      ' ', 'A', ' ', '4', ' ', '1', ' ', 'G', ' ', '1', ' ', '1', ' ', 'E', ' ', 'I', ' ', 'D', ' ', 'D', ' ', '9', ' ', 'G', ' ', '0', ' ', 'X', ' ', 'G', ' ', 'B']
print(''.join(m))
print(''.join(m2))
'''test case

Random test 11: ['0', ' ', 'c', ' ', 'o', ' ', 'f', ' ', 'i', ' ', '8', ' ', 'j', ' ', 'j', ' ', 's', ' ', 'q', ' ', 'f', ' ', '2', ' ', '3', ' ', 'q', ' ', 'k', ' ', 'g', ' ', 'a', ' ', '4', ' ', '1', ' ', 'g', ' ', '1', ' ', '1', ' ', 'e', ' ', 'i', ' ', 'd', ' ', 'd', ' ', '9', ' ', 'g', ' ', '0', ' ', 'x', ' ', 'g', ' ', 'b']
should equal ['0', ' ', 'C', ' ', 'O', ' ', 'F', ' ', 'I', ' ', '8', ' ', 'J', ' ', 'J', ' ', 'S', ' ', 'Q', ' ', 'F', ' ', '2', ' ', '3', ' ', 'Q', ' ', 'K', ' ', 'G', ' ', 'A', ' ', '4', ' ', '1', ' ', 'G', ' ', '1', ' ', '1', ' ', 'E', ' ', 'I', ' ', 'D', ' ', 'D', ' ', '9', ' ', 'G', ' ', '0', ' ', 'X', ' ', 'G', ' ', 'B']
14 Passed
'''
