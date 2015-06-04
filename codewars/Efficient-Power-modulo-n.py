
def power_mod(a, b, n):
    r = 1
    for i in xrange(b):
        r = r * a % n
    return r
print power_mod(2, 15, 300)
def modexp_rl(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1: # b is odd
            r = r * a % n
        b /= 2 # b is even
        if b == 0:
            break
        a = a * a % n # square a

    return r
print power_mod(2, 15, 300)
print pow(11, 10) % 300
