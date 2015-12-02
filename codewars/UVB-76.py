

import string


def validate(message):
    line = message.split()
    # print line
    if len(line) != 8:
        return False
    if line[0] != 'MDZHB':
        return False
    if len(line[1]) != 2:
        return False
    if len(line[2]) != 3:
        return False
    if any([ch not in string.ascii_uppercase for ch in line[3]]):
        return False
    if any([len(x) != 2 for x in line[4:]]):
        return False
    return True


class Test:

    @staticmethod
    def assert_equals(a, b):
        if a != b:
            print 'not pass'
        else:
            print 'pass'


# print validate("MDZHB 85 596 KLASA 81 00 02 91")

Test.assert_equals(validate("Is this a right message?"), False)
Test.assert_equals(validate("MDZHB 85 596 KLASA 81 00 02 91"), True)
Test.assert_equals(validate("MDZHB 12 733 EDINENIE 67 79 66 32"), True)
Test.assert_equals(validate("MDZHV 60 130 VATRUKH 58 89 54 54"), False)
