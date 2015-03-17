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

def isPP(n):
    from collections import Counter
    from functools import reduce
    factor_list = prime_factors(n)
    if len(set(factor_list)) == 1 and len(factor_list) > 1:
        return [factor_list[0], len(factor_list)]
    c = Counter(factor_list)
    v = c.values()
    product = reduce(lambda x,y : x * y, c.keys())
    if max(v) == min(v):
        return [product, min(v)]
    return None

print(isPP(144))


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

def isPP(n):
    from collections import Counter
    from functools import reduce
    factor_list = prime_factors(n)
    if len(set(factor_list)) == 1 and len(factor_list) > 1:
        return [factor_list[0], len(factor_list)]
    c = Counter(factor_list)
    v = c.values()
    product = reduce(lambda x,y : x * y, c.keys())
    if max(v) == min(v) and len(factor_list) > 1:
        return [product, min(v)]
    return None