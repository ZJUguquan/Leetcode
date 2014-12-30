

def s(i):
    if i == 0:
        return 4
    else:
        return s(i - 1) ** 2 - 2


def lucas_lehmer(n):
    if n == 2:
        return True
    m = 2 ** n - 1
    s = 4
    for i in range(2, n):
        sqr = s * s
        r = (sqr & m) + (sqr >> n)
        if r >= m:
            r -= m
        s = r - 2
    return s == 0


def lucas_lehmer(p):
    if p == 2:
        return True
    s = 4
    M = 2 ** p - 1
    for i in range(p - 2):
        s = divmod(s * s - 2, M)[1]
    if s == 0:
        return True
    else:
        return False

print(lucas_lehmer(7))
print(lucas_lehmer(3))
