def isInsect(i1, i2):
    a, b = i1
    c, d = i2
    if (a >= c and a < d) or (c >= a and c < b):
        return True
    return False


def union(i1, i2):
    a, b = i1
    c, d = i2
    if isInsect(i1, i2):
        return [min(a, c), max(b, d)]
