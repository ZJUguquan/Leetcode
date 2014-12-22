# #  通过此例子 好好的 最后一次学习 itertools permutations, product, repeat


# from itertools import permutations
# from itertools import groupby
# def fac(n):
#     if n <=2:
#         return n
#     return n * fac(n-1)

# def listPosition(word):
#     """Return the anagram list position of the word"""
#     # wordsorted = sorted(word)
#     wordsorted = ''.join(sorted(word))
#     n_letters = sorted(set(word))
#     n = len(n_letters)
#     print(n_letters)
#     res = {}
#     pool = 0
#     for idx, letter in enumerate(word):
#         if idx == 0:
#             res[0] = n_letters.index(letter) + 1
#             pool += (res[0] - 1) * fac(n-idx - 1)

#         if idx == 1:
#             res[1] = n_letters.index(letter) + 1
#             pool +=  (res[1] - 1) * fac(n-idx -1)
#             print(res)
#             print(pool)
#     # for k, g in groupby(wordsorted):
#     #     print(list(g))
#     pool = []
#     for e in permutations(wordsorted):
#         f = ''.join(e)
#         if f not in pool:
#             pool.append(f)
#         if f == word:
#             return len(pool)
#     return
#         # print(f)
#     # i =  1
#     # b = next(a)
#     # if b == word:
#     #     return i
#     # while b != word:
#     #     b = next(a)
#     #     i += 1
#     # return i
#     # return wordsorted, word


# print(listPosition('QUESTION'))

# '''test case

# test.describe('Anagram')
# test.it('Must return appropriate values for known inputs')
# testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
# for word in testValues:
#   test.assert_equals(listPosition(word), testValues[word], 'Incorrect list position for: ' + word)

#   '''

import math

# def getPermutation(n, target, k=1):
#     wordsorted = sorted(word)
#     n = len(wordsorted)
#     array = list(range(1, n + 1))
#     k = (k % math.factorial(n)) - 1
#     permutation = []
#     for i in range(n - 1, -1, -1):
#         idx, k = divmod(k, math.factorial(i))
#         permutation.append(array.pop(idx))
#     return "".join(map(str, permutation))


# print(getPermutation(5, 43))

from functools import reduce


def listPosition(word='QUEUS'):
    wordsorted = sorted(word)
    if word == ''.join(wordsorted):
        return 1
    n = len(wordsorted)
    location = []
    for i in word:
        loc = wordsorted.index(i)
        location.append(loc + 1)
        idx = wordsorted.index(i)
        # wordsorted[idx] = None
    # print(wordsorted)
    print(location)
    res = 0
    for idx, order in enumerate(location, start=1):

        res += (order - 1) *  math.factorial(n - idx )
        print(idx, order, word[idx-1], res)
            #reduce(lambda x,y:x*y, location[1+idx:])
            #* math.factorial(n - idx - 1)
        # else:
        #     res += (location[-1] -1)
    return res


word='QUESTION' # 24572
print(listPosition(word))




# from itertools import permutations
# from itertools import groupby

# def listPosition(word):
#     """Return the anagram list position of the word"""
#     # wordsorted = sorted(word)
#     wordsorted = ''.join(sorted(word))
#     pool = []
#     for k, g in groupby(list(permutations(wordsorted))):
#         # f = ''.join(e)
#         kk = ''.join(k)
#         if kk not in pool:
#             pool.append(kk)
#             # print(kk)
#         if kk == word:
#             return len(pool)
#         # pass
#         # if f not in pool:
#         #     pool.append(f)
#         # if f == word:
#         #     return len(pool)


# print(
# listPosition('QUESTION')
# )
# # print('AABB')