# Description:

# A Hamming number is a positive integer of the form 2i3j5k, for some
# non-negative integers i, j, and k.

# Write a function that computes the nth smallest Hamming number.

# Specifically:

# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in example test fixture.

# Your code should be able to compute all of the smallest 5,000 Hamming
# numbers without timing out.


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
    return res


def invalid(n):
    if any([i not in (2, 3, 5) for i in prime_factors(n)]):
        return False
    return True

# print(invalid(24))


def hamming(n):
    h = list(range(1, 1000000))
    h = [i for i in h if invalid(i)]
    print(h[n-1])
    print(len(h))
hamming(100)
