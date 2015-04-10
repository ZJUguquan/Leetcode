http://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python


-- 别人 5 6 行的代码


from math import ceil, log, sqrt

def isPP(n):
    for b in xrange(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None





-- 怎么时间要那么久.


def prime_factors(n):
    f, res = 3, []
    # if is_prime(n):
    #     return [n]
    while n % 2 == 0:
        res.append(2)
        n //= 2

    while f * f <= n:
        while n % f == 0:
            res.append(f)
            n //= f
        f += 2
    if n > 1:
        res.append(n)
    res.sort()
    return res

from collections import Counter
from functools import reduce
from fractions import gcd

# def is_perfect_power(n):
#     return reduce(gcd, Counter(factor(n)).values()) > 1

import operator

def isPP(n):
    factorlist = prime_factors(n)
    counter = Counter(factorlist)
    gcd_number = reduce(gcd, counter.values())
    factorset = set(factorlist)
    if gcd_number > 1:

        return [ reduce(operator.mul, [ i ** (factorlist.count(i) // gcd_number)  for i in factorset]) , gcd_number]
    return None

n = 6
print(isPP(n))


