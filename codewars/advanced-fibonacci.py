# coding: utf-8


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]


# Example 1: Using looping technique
@Memoize
def fib(n):
    if n < 0: raise ValueError('n is Postive!!!')
    if n < 2: return n
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def productFib(prod):
    su = 0
    i = 0
    while su < prod:
        i += 1
        su += fib(i) ** 2
        if su == prod:
            two_product = fib(i+1) * fib(i)
            return [fib(i), fib(i+1), two_product == prod]
        elif su > prod:
            return [fib(i), fib(i+1), False]
    return

print productFib(4895)
print productFib(203023208030065646654504166904697594722575)

#Test not pass
# [354224848179261915075L, 573147844013817084101L, False] should equal [573147844013817084101L, 927372692193078999176L, False]

s = 354224848179261915075L * 573147844013817084101L
print s