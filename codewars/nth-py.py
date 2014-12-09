def nth_fib(n):
    if n == 1 or n == 2:
        return n - 1
    m = 1 ; a = 0; b = 1
    while m < n:
        a, b = b, a + b
        m += 1
    return a

print(nth_fib(10))