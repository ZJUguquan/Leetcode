<<<<<<< HEAD
# # p is odd, (x- 1) ^p -(x^p -1)
# from functools import reduce
# factorial = lambda x: reduce(int.__mul__, range(2, x + 1), 1)
# print(fact(10))
# def factorial(k):
# 	if k <= 1:
# 		return 1
# 	else:
# 		return k*factorial(k-1)

# def choose(n, k):
# 	if n == k or k == 0:
# 		return 1
# 	else:
# 		return int(factorial(n)/factorial(k)/factorial(n-k) )

# print(choose(10, 3))
from itertools import combinations
choose = lambda n, r: len( list( combinations(list(range(n)), r)) )

def aks_test(p):
	if 2<= p <= 3:
		return True
	if p <= 1 or p % 2 == 0:
		return False
	for i in range(1, p):
		coeff =	choose(p, i)
		if coeff % p != 0:
			return False
	return True

from unittest import TestCase

test = TestCase()


print(aks_test(10))

test.assertEqual(aks_test(7), True)
test.assertEqual(aks_test(10), False)

test.assertEqual(aks_test(19), True)
=======
'other solution'
import math

def aks_test(p):
    if p == 1:
        return False
    for comb in combinations(p):
        if comb % p != 0:
            return False
    return True

def aks_test(p):
    coeff = 1
    for i in xrange(p / 2):
        coeff = coeff * (p - i) / (i + 1)
        if coeff % p:
            return False
    return p > 1

#generator returns list of coefficients in first-half of polynomial expansion
#(second-half of expansion will be duplicates)
def combinations(n):
    i = 0
    c = 1
    for i in range(n / 2):
        c *= (n - i)
        c /= i + 1
        yield c




from functools import reduce

# def prod(a, b):
#     return a * b


def aks_test(p):
    if p % 2 == 0 and p > 3 or p < 2:
        return False
    if p in [2, 3, 5]:
        return True
    cache = [p]; small = [1]
    for i in range(0, p//2):
        cache.append( cache[-1] * (p-i-1))
        small.append( small[-1] * (i+2))
        if cache[-1] % (p* small[-1]) != 0:
            return False

    # print(cache, small)
    return True


print(aks_test(13))

# for i in range(10,20):
#     print(aks_test(i))




    # cache = [ p - i for i in range(0, p//2)]
    # smallnumber = [ i + 1 for i in range(0, p//2 + 1)]
    # # the binominal coeffiicients 2nd - mid item.
    # for i in range(1, p//2 + 1):
    #     if reduce(prod, cache[:i]) % (p * reduce(prod, smallnumber[:i]) ) != 0:
    #         return False
    # return True

# def aks_test(p):
#     if p % 2 == 0 and p > 3 or p < 2:
#         return False
#     if p in [2, 3, 5]:
#         return True
#     cache = [ p - i for i in range(0, p//2)]
#     smallnumber = [ i + 1 for i in range(0, p//2 + 1)]
#     # the binominal coeffiicients 2nd - mid item.
#     for i in range(1, p//2 + 1):
#         if reduce(prod, cache[:i]) % (p * reduce(prod, smallnumber[:i]) ) != 0:
#             return False
#     return True
>>>>>>> 945ccf904bd98fd546abce5b9864da977440b7d3
