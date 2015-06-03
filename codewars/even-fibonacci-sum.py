
# http://www.codewars.com/kata/55688b4e725f41d1e9000065/train/python

class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def even_fib(m):
    i = 1
    sums = 0
    while fib(i) < m:
        if fib(i) % 2 == 0:
            sums += fib(i)
        i += 1
        if fib(i) > m:
            break
    return sums


assert even_fib(0) == 0
assert even_fib(1) == 0
assert even_fib(5)# == 2
print even_fib(10)# == 10
print even_fib(33)# == 10
print even_fib(25997544)# == 19544084


assert even_fib(0) == 0
assert even_fib(1) == 0
assert even_fib(5) == 2
assert even_fib(10) == 10
assert even_fib(33) == 10
assert even_fib(25997544) == 19544084


'''
Give the summation of all even numbers in a Fibonacci sequence up to, but not including, the maximum value.

The Fibonacci sequence is a series of numbers where the next value is the addition of the previous two values. The series starts with 0 and 1:

0 1 1 2 3 5 8 13 21...
'''
