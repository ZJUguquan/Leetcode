from math import sqrt
from math import floor, ceil


def prime_squares(p):
    for i in range(1, 100, 2):
        if p >= i*i:
            if floor(sqrt(p-i*i)) == ceil(sqrt(p-i*i)):
                return (i, int(sqrt(p-i*i)))