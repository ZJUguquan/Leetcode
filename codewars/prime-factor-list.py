
def is_prime(n):
    '''
    check it is prime number
    '''
    return n > 1 and all(n % i for i in range(2, n))


def prime_factors(n):
    res = []
    if is_prime(n):
        return [n]
    factor_list = [i for i in range(int(n//2), 1, -1) if is_prime(i)]
    curr = 0
    while n > 1:
        while n % factor_list[curr] == 0:
            n = n // factor_list[curr]
            res.append(factor_list[curr])
        curr += 1
    return res[::-1]

print(prime_factors(1001))
