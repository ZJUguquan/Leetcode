
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]


@Memoize
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

# print(fib(4), fib(3))

def perimeter(n):
    if n < 2:
        return 4 * (n+1)
    if n >= 3:
        return fib(n+1) * fib(n)

print(perimeter(5))

