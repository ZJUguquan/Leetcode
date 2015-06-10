def validate_ean(code):

    sum = 0
    for idx, i in enumerate(code[:-1]):
        if int(idx) % 2 == 0:
            sum += int(i)
        else:
            sum += int(i) * 3

    return  (10 - sum % 10) % 10 == int(code[-1])


print validate_ean('4003301018398')

from unittest import TestCase


class MyTest(object):
    def assert_equals(self, c1, c2, msg='-----'):
        if c1 == c2:
            print 'Test passssssssssssssssssssssssssssssssssssssss'
        else:
            print 'EEEEEEEEEEEEEEEEEEE'+ msg

test = MyTest()


test.assert_equals(validate_ean("9783815820865"), True)
test.assert_equals(validate_ean("9783815820864"), False)
test.assert_equals(validate_ean("9783827317100"), True)
