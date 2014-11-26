'better solution'

import __builtin__

class CustomList(list):
    def ints(self):
        return [x for x in self if isinstance(x, int)]
    def even(self):
        return [x for x in self.ints() if x % 2 == 0]
    def odd(self):
        return [x for x in self.ints() if x % 2 == 1]
    def under(self, ceil):
        return [x for x in self.ints() if x < ceil]
    def over(self, floor):
        return [x for x in self.ints() if x > floor]
    def in_range(self, min, max):
        return [x for x in self.ints() if min <= x <= max]


class list(object):

    def __init__(self, args):
        self.stack = args
        # for ele in args:
            # self.stack.append(ele)

    def even(self):
        return [ele for ele in self.stack if isinstance(ele,int) and ele%2 == 0]

    def odd(self):
        return [ele for ele in self.stack if isinstance(ele,int) and ele%2 == 1]

    def under(self, underbond):
        return [ele for ele in self.stack if isinstance(ele,int) and  ele<underbond]

    def over(self, overbond):
        return [ele for ele in self.stack if isinstance(ele,int) and  ele > overbond]

    def in_range(self, left, right):
        return [ele for ele in self.stack if isinstance(ele,int) and  right>=ele and ele >= left]



t = list([1,2,3,4,5])

t = list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11])
print(t.stack)

print("even",t.even())
print("odd",t.odd())
print(t.under(3))
print(t.over(4))
print(t.in_range(1,3))
