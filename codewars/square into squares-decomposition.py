# -*- coding: utf-8 -*-

la = """
Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return the result with the largest possible values:

Examples:

decompose(11) must return [1,2,4,10] 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doen't form a strictly increasing sequence.

Note: Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None or "".

The function "decompose" will take a positive integer n and return the decomposition of N = n² as
"""
from math import sqrt
from math import floor, ceil

def decompo(n):
    if n == 0:
        return None
    if n == 1:
        return [1]
    # if n == 5:
    max_number = int(floor(sqrt(n)))
    if n == max_number ** 2:
        max_number -= 1
    while (n - max_number**2) > 0:
        delta = n - max_number ** 2
        if max_number < 2:
            return None
        if decompo(delta) is None :
            max_number -= 1
        else:
            if ceil(sqrt(delta)) == int(floor(sqrt(delta))):
                return [int(floor(sqrt(delta))), max_number]
            else:
                if max_number not in decompo(delta):
                    return sorted(decompo(delta) + [max_number])
                else:
                    #continue
                    max_number -= 1

    return None

# print(decompo(104))

def decompose(n):
    return decompo(n*n)


# print(decompose(5))
# print(decompo(124))
# print(decompo(72))
print(decompo(38))
#  7532  4 + 9 + 25 + 49
# print(decompose(44))
# print( 1936 - 43* 43)