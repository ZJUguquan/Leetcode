def loop(a):
    a = a % 10
    if str(a) in ('0', '1', '5', '6'):
        return 1

    i = 2
    now = a * a % 10

    while now != a:
        now = now * a % 10
        i += 1
    return i - 1


def last_digit(a, b):
    a = int(str(a)[-1])
    b = b % loop(a)
    if str(a) in ('0', '1', '5', '6') or b == 1:
        return a

    i = 2
    now = a * a % 10

    while i < b:
        now = now * a % 10
        i += 1
    return now
