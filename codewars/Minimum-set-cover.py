
secret = 'w1ZJzgjWykaDPeNSm76upIx53E9FGVhTcQMXOtvBHUqLsKfo02lrC4YndbiRA8'
cover_set = [   ['0', '2', 'l'],
    ['3', 'E', '9'],
    ['6', 'u', 'p'],
    ['B', 'H', 'U'],
    ['F', 'G', 'V'],
    ['I', 'x', '5'],
    ['J', 'z', 'g'],
    ['K', 'f', 'o'],
    ['O', 't', 'v'],
    ['P', 'e', 'N'],
    ['Q', 'M', 'X'],
    ['R', 'A', '8'],
    ['S', 'm', '7'],
    ['Y', 'n', 'd'],
    ['b', 'i', 'R'],
    ['h', 'T', 'c'],
    ['j', 'W', 'y'],
    ['k', 'a', 'D'],
    ['q', 'L', 's'],
    ['r', 'C', '4'],
    ['w', '1', 'Z']]

from pprint import pprint
pprint(sorted(cover_set), indent=4)

print len(cover_set)

# description of this kata:

This is an ataK, a reverse Kata. First, solve "Recover a secret string from random triplets". Then write a test generator for that Kata: given a random string whit no characters repetitions, find out the minimun set of triplets which is sufficient to recover the original string using a solution from the previous Kata.












# def cover(secret, cover=cover_set):
#     '''
#     return minimum subset-number (each subset has 3 elements - different)
#     '''
#     s = set(secret)
#     for idx, each_set in enumerate(cover_set):
#         # special cases -  . << ...
#         if set(secret) & (set(each_set)) is None:
#             cover_set.pop(idx)
#             continue
#         if set(secret).issubset(set(each_set)):
#             return 1

#         else:
#             # use this or not
#             use_it = 1 + cover(set(secret)-set(each_set), cover=cover_set[0:idx-1]+cover_set[idx+1:])
#             not_use = cover(secret, cover=cover_set[0:idx-1]+cover_set[idx+1:])
#             return min(use_it, not_use)

# secret = 'abcdef'
# coverset=[ ['a','b','c'], ['d','e','f']
# ]
# print cover(secret, coverset)



