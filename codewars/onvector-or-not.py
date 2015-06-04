# coding: utf-8





########################################################################


class Test(object):
    def assert_equals(self, left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
test = Test()


def side(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1] -p2[1])**2 )**.5

def point_in_vector(point, vector):
    if point in vector:
        return True
    s1 = side(point, vector[0])
    s2 = side(point, vector[1])
    s = side(vector[0], vector[1])
    print s1 + s2 -  s
    return abs(s1 + s2 - s) < 10 ** -6


from unittest import TestCase


class MyTest(object):
    def assert_equals(self, c1, c2, msg='-----'):
        if c1 == c2:
            print 'Test passssssssssssssssssssssssssssssssssssssss'
        else:
            print 'EEEEEEEEEEEEEEEEEEE'+ msg


Test = MyTest()

point = [1, 1]
vector = [[0, 0], [3, 3]]
Test.assert_equals(point_in_vector(point, vector), True)

point = [2, 2]
vector = [[0, 0], [1, 1]]
Test.assert_equals(point_in_vector(point, vector), False)

point = [5, 4]
vector = [[2, -3], [5, 4]]
Test.assert_equals(point_in_vector(point, vector), True)

point = [2, 3]
vector = [[2, 3], [2, 3]]
Test.assert_equals(point_in_vector(point, vector), True)

point = [1, 5]
vector = [[1, -3], [1, 7]]
Test.assert_equals(point_in_vector(point, vector), True)

point = [3, 5]
vector = [[-2, 5], [10, 5]]
Test.assert_equals(point_in_vector(point, vector), True)