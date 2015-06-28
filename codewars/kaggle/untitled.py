



n = 52

from itertools import combinations

# print len( list(combinations(range(52), 41)))


from math import factorial

print  factorial(52)/( factorial(41)*factorial(11))


def find_dup(arr):
    #your code here
    pool = []

    for idx in range(len(arr)//2):
        if arr[idx] not in pool:
            pool.append(arr[idx])
        else:
            return arr[idx]

        if arr[-idx-1] not in pool:
            pool.append(arr[-idex-1])
        else:
            return arr[-idex-1]

