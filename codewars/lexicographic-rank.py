'Lexicographic rank of permutation'

from math import factorial


def findPermutation(s, rank):
    n = len(s)
    step = factorial(n)
    perm = ''
    s = sorted(s)
    # if rank == 0:
    #     return s
    index = 0
    for i in range(0, n):
        step /= (n - i)
        index = int((rank) // step)
        # if index > 0:
        perm += s[index]
        s = s[:index] + s[index+1:]
        rank -= (index) * step
        # else:  # index == 0
        #     perm += s[0]
        #     s = s[1:]
        # print(perm, '\t***', rank)
    return perm

print(findPermutation('cba', 0))

print(findPermutation("57133044", 9999))