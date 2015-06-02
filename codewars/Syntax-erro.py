from functools import partial


class Foo(object):

    def __init__(self):
        self.func = int
        self.arr_of_funcs = [
            partial(int, base=2)
            partial(int, base=8)
        ]

    def convert(self, num, base):
        return self.arr_of_funcs[base](num)


class Test(object):

    def assert_equals(self, left, right, msg):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!', msg
test = Test()

f = Foo()
Test.assert_equals(
    f.convert('0', 0), 0, "zero convert to an integer in any base is 0")
Test.assert_equals(
    f.convert('0', 1), 0, "zero convert to an integer in any base is 0")
