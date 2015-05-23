
def permutations(l):
    res = []
    if len(l) <= 1:
        yield l
    else:
        for perm in permutations(l[1:]):
            for i in range(len(l)):
                yield perm[:i] + l[0:1] + perm[i:]
