
# coding: utf-8


## Example 5: Using memoization as decorator


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]

def o(msg=None):
    print( ('*'*30+str(msg)+'*'*30).center(80))

@Memoize
def factorial(n):
    # do it
    if n < 2: return 1
    return n * factorial(n-1)

print factorial(100)

factorial_memo = {}
def factorial(k):
    if k < 0:
        return None
    if k < 2:
        return 1
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

print factorial2(200)