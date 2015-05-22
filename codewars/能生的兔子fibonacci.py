
class Memoize:

    def __init__(self, func):
        self.func = func
        self.memo = defaultdict(int)
        self.memo[0] = 1
        self.memo[1] = 1


    def __call__(self, n, b):
        self.memo[2] = 1 + b
        if n not in self.memo:
            self.memo[n] = self.func(n, b)
            return self.memo[n]


def fib_rabbits(n, b):
    if n in (0, 1):
        return 1
    p, q, i = 1, 0, 1
    while i < n:
        new_p = b * q
        new_q = p + q
        p, q = new_p, new_q
        i += 1
    return p + q

print fib_rabbits(6, 3)
print fib_rabbits(7, 4)
print fib_rabbits(8, 12)
oye()
test.assert_equals(fib_rabbits(6, 3), 4)

test.assert_equals(fib_rabbits(8, 12), 8425)
test.assert_equals(fib_rabbits(7, 4), 181)
