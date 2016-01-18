



import os
import sys

# print(os.environ)
print( [[] for i in range(10)]   )
def group_in_10s(*t):
    #your code here
    if not t: return []
    mm = max(t)

    bins  = mm // 10 + 1
    group = [ None for i in range(bins)]
    for i in sorted(t):
        if not group[i // 10]:
            group[i // 10] = []
    	group[i // 10].append(i)

    return group
print('haha')

import unittest
class Test(unittest.TestCase):
    @staticmethod
    def assert_equals(a, b, msg="Something happend. You fool!"):
        if a != b:
            print(a)
            print(b)
            print('error %s' % msg)
        print a == b
        print('-'*77)


Test.assert_equals(group_in_10s( 1,2,3 ), [ [ 1, 2, 3 ] ])
Test.assert_equals(group_in_10s( 8, 12, 38, 3, 17, 19, 25, 35, 50 ), [ [ 3, 8 ], [ 12, 17, 19 ], [ 25 ], [ 35, 38 ], None, [ 50 ]])
Test.assert_equals(group_in_10s( 12, 10, 11, 13, 25, 28, 29, 49, 51, 90 ), [ None, [ 10, 11, 12, 13 ], [ 25, 28, 29 ], None, [ 49 ], [ 51 ], None, None, None, [ 90 ] ])
Test.assert_equals(group_in_10s(), [])
Test.assert_equals(group_in_10s(100), [None, None, None, None, None, None, None, None , None, None, [ 100 ]])
