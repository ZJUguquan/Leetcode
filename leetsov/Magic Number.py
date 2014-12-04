#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'STEVE'

"""documents:
Magic Number
"""


print '2^2 = %d' % (2**2)
print '2^4 = %d' % (2**4)
print '2^8 = %d' % (2**8)
print '2^16 = %d' % (2**16)
print '2^32 = %d  4GB' % (2**32)
print '2^64 = %d' % (2**64)

print '2^2 = %d' % (2**2)
print '2^2 = %d' % (2**2)

'2-100 的质数'

print filter(lambda x: len(filter(lambda y: x%y == 0, range(2, x-1) ))==0, range(2,101) )



