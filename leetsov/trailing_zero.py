def trailing(n):
    result = 0
    while 5 < n:
        result += n//5
        n //= 5
    return result

r = 1800
print(trailing(r))
from math import factorial
print(factorial(r))