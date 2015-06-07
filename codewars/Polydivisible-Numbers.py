

def is_polydivisible(s, b):

    for idx, ele in enumerate(s):
        if int(s[:idx + 1], b) % (idx + 1) > 0:
            return False
    return True


# def get_polydivisible(n, b):
#     out = []
#     i = 0
#     while len(out) < n:
#         print '@@, ', str(i)
#         if not is_polydivisible(str(i), b):
#             i += 1
#             continue
#         else:
#             out.append(i)
#             i += 1
#     print out


def is_polydivisible(s, base=10):
    n = 0
    for (d, c) in enumerate(s, 1):
        n = n * base + CHARS.index(c)
        if n % d:
            return False
    return True

#
# Memory-devouring solution that tries to avoid checking numbers for polydivisibility,
# but instead generates polydivisible numbers.


def polydivisibles(base=10):
    cache = [('', 0), ]
    for (s, v) in cache:
        if s == '0':
            continue
        pos = len(s) + 1
        r = v % pos
        for n in xrange(pos - r if r else 0, base, pos):
            ret = s + CHARS[n]
            if pos < base:
                cache.append((ret, (v + n) * base))
            yield ret


def get_polydivisible(n, base=10):
    for (i, ret) in enumerate(polydivisibles(base), 1):
        if i == n:
            return ret


test = [('1232', 10), ('123220', 10), ('123220', 6)]
for arg in test:
    print is_polydivisible(arg[0], arg[1])


# get_polydivisible(22, 10)
get_polydivisible(42, 16)




















from collections import deque

def is_polydivisible(s, base=10):
    n = 0
    for (d, c) in enumerate(s, 1):
        n = n * base + CHARS.index(c)
        if n % d:
            return False
    return True

#
# Memory-devouring solution that tries to avoid checking numbers for polydivisibility,
# but instead generates polydivisible numbers.

def polydivisibles(base = 10):
    cache = deque((('', 0),))
    while True:
        (s, v) = cache.popleft()
        if s == '0':
            continue
        pos = len(s) + 1
        r = v % pos
        for n in xrange(pos - r if r else 0, base, pos):
            ret = s + CHARS[n]
            cache.append((ret, (v + n) * base))
            yield ret

def get_polydivisible(n, base = 10):
    for (i, ret) in enumerate(polydivisibles(base), 1):
        if i == n:
            return ret
