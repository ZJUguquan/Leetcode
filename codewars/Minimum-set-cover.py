
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

def generate_triplets(secret):
    lens = len(secret)
    secret = list(secret)
    output = []

    while len(secret) >=3:
        temp = []
        for _ in range(3):
            temp.append(secret.pop(0))
        output.append(temp)

    if len(secret) == 1:
        output.append([temp[-2], temp[-1], secret.pop(0)] )
    elif len(secret) == 2:
        output.append([temp[-1], secret.pop(0), secret.pop(0)] )
    return output










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



