# 通过此例子 好好的 最后一次学习 itertools permutations, product, repeat
# passed!
from math import factorial

def repeat_product(s):
    from collections import Counter
    c = Counter(s)
    # print(c)
    repeat_product = 1
    for k in c:
        repeat_product *= factorial(c[k])
    return repeat_product

def listPosition(word):
    s = word
    n = len(s)
    # print(factorial(n))
    rem = 1
    raw_order = sorted(s)
    # print(raw_order)
    for idx, letter in enumerate(s):
        l = len(raw_order)
        F = factorial(l)//repeat_product(raw_order)
        position = raw_order.index(letter)
        if position == 0:
            raw_order = raw_order[1:]
            continue
        rem += F//l*position
        raw_order = raw_order[:position] + raw_order[position+1:]
    return rem

print(listPosition('BAAA'))

# '''test case


# from itertools import permutations
# from itertools import groupby

# def listPosition(word):
#     """Return the anagram list position of the word"""
# wordsorted = sorted(word)
#     wordsorted = ''.join(sorted(word))
#     pool = []
#     for k, g in groupby(list(permutations(wordsorted))):
# f = ''.join(e)
#         kk = ''.join(k)
#         if kk not in pool:
#             pool.append(kk)
# print(kk)
#         if kk == word:
#             return len(pool)
# pass
# if f not in pool:
# pool.append(f)
# if f == word:
# return len(pool)

print('*'*40)
s = 'ABAB'

# print(repeat_product)
