

a1 = "Look mom, no hands"
a2 = "4c6f6f6b206d6f6d2c206e6f2068616e6473"
print(int('c', 16))
print(chr(95))
# print(ord('L'))
# for sn in range2(a2):
#   print(sn)
print(Converter.to_ascii(a2))
print(Converter.to_hex(a1))
# print(hex(255)[2:])

import unittest
class Test(unittest.TestCase):
    @staticmethod
    def assert_equals(a, b, msg=None):
        if a== b:
            print('aha')
        else:
            print('nonono')
s="Look mom, no hands"
h="4c6f6f6b206d6f6d2c206e6f2068616e6473"

Test.assert_equals(Converter.to_hex(s),h)
Test.assert_equals(Converter.to_ascii(h),s)
Test.assert_equals(Converter.to_hex(Converter.to_ascii(h)),h)
Test.assert_equals(Converter.to_ascii(Converter.to_hex(s)),s)
