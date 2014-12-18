# repeated substring

# def f(s):
#     from re import split
#     result = split(r'(\w{2,}?)', s)
#     print(result)

# f('abcabcabc')


# groupby

from itertools import groupby

print([ (k, list(g)) for k, g in groupby('AAAABBBCCDAABBB')] ) # --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D