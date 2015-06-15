# coding: utf-8


import sys
print sys.platform

class MyTest(object):
    def assert_equals(self, c1, c2, msg='-----'):
        if c1 == c2:
            print 'Test passssssssssssssssssssssssssssssssssssssss'
        else:
            print c1, c2
            print 'EEEEEEEEEEEEEEEEEEE'+ msg
        print '-' * 67

Test = MyTest()


def flatten(container):

    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i


def list_to_array(nests):
    if nests is None:
        return []
    return list(flatten(nests))


u = None
Test.assert_equals(list_to_array(u), [])

u = List(4, List(25, List(30)))
Test.assert_equals(list_to_array(u), [4, 25, 30])

u = List(2, List(40, List(43, List(25, List(125)))))
Test.assert_equals(list_to_array(u), [2, 40, 43, 25, 125])
