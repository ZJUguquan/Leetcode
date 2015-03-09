
# def is_prime(n):
#     '''
#     check it is prime number
#     '''
#     return n > 1 and all(n % i for i in range(2, n))


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

print(prime_factors(240))
