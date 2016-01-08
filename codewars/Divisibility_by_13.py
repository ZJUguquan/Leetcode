

import itertools as it


def thirt(n):
    if n < 100:
        return n

    pattern = it.cycle([1, 10, 9, 12, 3, 4])

    return thirt(sum(d * n for d, n in zip(map(int, str(n)[::-1]), pattern)))


# =============================================================================
def thirt(n):
    rs = [1, 10, 9, 12, 3, 4]
    digits = map(int, str(n))[::-1]
    lenth = len(digits)
    drs = rs * lenth
    sum = 0

    for idx, i in enumerate(digits):
        # print(i, drs[idx])
        sum += i * drs[idx]
    if sum != n:
        return thirt(sum)
    return sum

print thirt(8529)
