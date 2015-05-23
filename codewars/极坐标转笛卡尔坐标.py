
import decimal

d = decimal.Decimal('123.456123789123321')

for i in range(8, 11):
    decimal.getcontext().prec = i
    print i, ':', d, d * 1


print str(d)
s = '%.10f' % d

print float(s)

change = lambda x: float('%.10f' % x)

print change(d)


change = lambda x: float('%.10f' % x)

from math import sin, cos, pi


def coordinates(degrees, r):
    c, s = r * cos(degrees * pi / 180), r * sin(degrees * pi / 180)

    return (change(c), change(s))
