# coding: utf-8


import operator

########################################################################


class Test(object):
    def it(self, msg):
        print msg


    def describe(self, msg):
        print msg

    def assert_equals(self, left, right, msg=None):
        if left == right:
            print left, 'done'
        else:
            print msg

    def assert_true(self, left, right=True, msg=None):
        if left == right:
            print left, 'done'
        else:
            print msg


test = Test()


class Anything(object):
    def __init__(self):
        self.id = 1

def anything(pa):
    return Anything()


from operator import *
def __gt__(a, b):
    if type(a) == Anything or type(b) == Anything:
        return True
    return a >= b



test.describe("Anything can be true")


import re
import mat
h
test.it("A module re is greater than re")
test.assert_true(anything(re) >= re)



# test.it("An dectionary is not equal to an Array")
# test.assert_true(anything({}) != [])

# test.it("The string Hello is less than world")
# test.assert_true(anything('Hello') < 'World')

# test.it("80 is greater than 81")
# test.assert_true(anything(80) > 81)


# test.it("A module re is less than or equal to the module math")
# test.assert_true(anything(re) <= math)

# test.it("A number 5 is equal to an undifined varaible")
# test.assert_true(anything(5) == ord)


def converter(mpg):
    #your code here
    return round(mpg / 4.54609188 * 1.609344    , 2)

print converter(12)