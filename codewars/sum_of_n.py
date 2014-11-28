'''
sum_of_n (or SequenceSum.sumOfN in Java) takes an integer n and returns a List of length abs(n) + 1. The List contains the numbers in the arithmetic series produced by taking the sum of the consecutive integer numbers from 0 to n inclusive.
'''


'clever'

def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]

def sum_of_n(n):
    res = [];
    if n >= 0:
        for i in range(0,n + 1):
            res.append(i*(i+1)//2)
    else:
        for i in range(0, n-1, -1):
            res.append(-i*(i-1)//2)
    return res

print(sum_of_n(10))
print(sum_of_n(-10))

