
from functools import reduce
from operator import mul
from collections import Counter


def is_palindrome(num):
    if len(str(num)) == 1 or (len(str(num)) == 2 and str(num)[0] == str(num)[-1]):
        return True
    if str(num)[0] != str(num)[-1]:
        return False
    return int(str(num)[1:-1])

def palindrome(s):
    digits = sorted(map(int, list(s)), reverse=True)

    occur_2 = sorted([d for d in digits if digits.count(d) >= 2], reverse=True)
    out = []
    while len(occur_2) > 0:
        first = occur_2.pop(0)
        if first in occur_2:
            mid = len(out) // 2
            out.insert(mid, first)
            out.insert(mid+1, occur_2.pop(0))
        else:
            continue
    odds = [i for i in digits if digits.count(i) % 2 == 1]
    if out.count(0) == len(out): out = []
    if len(odds) > 0:
        odd_as_mid = max(odds)
        out.insert(len(out)//2, max(odds))

    return int(''.join(map(str, out)))



def numeric_palindrome(*args):
    out = []
    for num in args:
        if is_palindrome(num):
            out.append(num)
    from itertools import combinations
    lens = len(args)
    for r in range(2, lens+1):
        combinator = combinations(args, r)
        for each in combinator:
            product = reduce(mul, list(each))
            out.append(palindrome(str(product)))

    return max(out)