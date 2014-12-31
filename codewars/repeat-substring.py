def factors(n):
    '''Generate all  factors of n.'''
    return [i for i in range(1, n//2+1) if n % i == 0]


def f(s):
    n = len(s)
    if n == 0:
        return ''
    if s == s[0] * n:
        return (s, n)

    fac = factors(n)[::-1]
    for group_pos in fac:
        if s == s[:(n//group_pos)] * group_pos:
            return (s[:(n//group_pos)], group_pos)
    return (s, 1)

# print(prime_factors(8))
print(factors(24))
print(f('abababab'))
print(f('abcde'))