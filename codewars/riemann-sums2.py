

# from __future__ import division

def left_riemann(f, n, a, b):
    # left side rule
    sum = 0
    step = (b-a) / float(n)
    print 'step: %s' % step
    left, right = a, a+step
    i = 0
    while i < n:
        sum += f(left) * step
        left, right = right, right+step
        i += 1
    return round(sum, 2)
    return  #round(sum, 2)

quadratic = lambda x: round(100 * x * x)/100
print left_riemann(quadratic, 10, 0, 1)


# f(x) = x^2 with n = 10 on [0, 1]: 0.0 should equal 0.29

i = 1

from time import time, sleep
while i < 100:
    print i,'a',
    sleep(2)
    i += 1