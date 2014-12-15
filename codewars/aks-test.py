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