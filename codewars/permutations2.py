def permutations(strng):
    if len(strng) == 1:
        return list(strng)
    head = strng[0]
    result = []
    lens = len(strng)
    for left in permutations(strng[1:]):
        for i in range(lens):
            ma = left[:i] + head + left[i:]
            if ma not in result:
                result.append(ma)
    return result

print permutations('ab')



def permutations(string):
    from itertools import permutations as perm
    return set(map(lambda x: "".join(x), perm(string)))