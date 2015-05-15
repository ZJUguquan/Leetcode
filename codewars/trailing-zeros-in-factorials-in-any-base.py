
# http://www.codewars.com/kata/544483c6435206617a00012c/discuss
# 18, 12
from collections import defaultdict

def trailing_zeros(num, base):
    factors = defaultdict(int)
    p = 2
    while base > 1:
        d, m = divmod(base, p)
        if m == 0:
            base = d
            factors[p] += 1
        else:
            p += 2 - int(p==2)
    # calculate the number of zeroes
    zeroes = None
    for p in factors:
        c, q = 0, p
        while q <= num:
            c += num // q
            q *= p
        c //= factors[p]
        if zeroes is None or zeroes > c:
            zeroes = c
    return zeroes

print trailing_zeros(7 , 21)
print trailing_zeros(15, 10)
print trailing_zeros(15, 12)