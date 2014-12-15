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
