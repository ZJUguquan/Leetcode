'generic number class'

"""
Your task in this kate is to implement function create_number_class which will take parameter alphabet (string) and return class representing number composed of this alphabet.

The number class will implement four arithmetic operations: +, -, *, // and method convert_to which will take other number class as parameter and will return instance of the other class with same value as itself.

Example:
bin = create_number_class('01')
hex = create_number_class('0123456789ABCDEF')

x = bin('1010')
y = bin('10')

print x + y # 1100
print x.convert_to(hex) # A
"""


def create_number_class(alphabet):
    n = len(alphabet)

    class Number(object):

        def __init__(self, s):
            if isinstance(s, str):
                v = 0
                for c in s:
                    v = v * n + alphabet.index(c)
            else:
                v = s
            self.value = v

        def __add__(self, other):
            return Number(self.value + other.value)

        def __sub__(self, other):
            return Number(self.value - other.value)

        def __mul__(self, other):
            return Number(self.value * other.value)

        def __floordiv__(self, other):
            return Number(self.value // other.value)

        def __str__(self):
            ret = []
            v = int(self.value)
            while v:
                (v, r) = divmod(v, n)
                ret.append(alphabet[r])
            return ''.join(reversed(ret or alphabet[0]))

        def convert_to(self, cls):
            return cls(self.value)

    return Number


bin = create_number_class('01')
x = bin('1011')
y = bin('10')
print(x + y)
hex = create_number_class('0123456789ABCDEF')
print(x.convert_to(hex))
