# coding: utf-8
def make_lazy(*args):
    paras = args[1:]
    return args[0].__call__(*paras)


def modding(a,b):
    return a%b

from random import randint
lazy_mod= make_lazy(modding,4,4)
# test.assert_equals(lazy_mod(),0)
rand_num = randint(0,10)
rand_num2 = randint(0,10)
lazy_rand = make_lazy(modding,rand_num,rand_num2)


print(rand_num, rand_num2)
print(lazy_mod)
print(modding(rand_num, rand_num2))
print(lazy_rand == modding(rand_num, rand_num2))
