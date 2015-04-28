
# def is_prime(n):
#     '''
#     check it is prime number
#     '''
#     return n > 1 and all(n % i for i in range(2, n))


def prime_factors(n):
    if n <= 0 :
        n = -n
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

print(prime_factors(-61548))


def number_property(n):
    return [isPrime(n), isEven(n), isMultipleOf10(n)]
    # Return isPrime? isEven? isMultipleOf10?
    #your code here

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isEven(n):
    return n % 2 == 0

def isMultipleOf10(n):
    return n % 10 == 0
# from collections import Counter
# c = Counter(prime_factors(216))
# print(c)
# print(c.values())

# print(max(c.values()), min(c.values()))
# from functools import reduce
# print(reduce(lambda x,y : x * y, [1,2,3,4]))
# from math import sqrt, floor
# print(sqrt(44944) == floor(sqrt(44944)))