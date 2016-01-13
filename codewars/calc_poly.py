

formaat = lambda x : ' ' + x[0] + ' ' + x[1:]

def calc_poly(pol_list, x): #If polynomial degree == 3
    lens = len(pol_list)
    if not pol_list:
        return ''
    if pol_list[0] == 0:
        return calc_poly(pol_list[1:], x)
    output, value = 'For ', 0
    for idx, ele in enumerate(pol_list):
        if ele == 0:
            continue
        if idx == 0:
            if ele != 1:
                output += '{0:-}*x^{1} '.format(ele, lens-1-idx)
            else:
                output += 'x^{0} '.format(lens-1-idx)
        elif idx < (lens-2):
            output += formaat('{0:+}*x^{1} '.format(ele, lens-1-idx))

        elif idx == (lens-2):
            output += formaat('{0:+}*x '.format(ele))
        else:
            output += formaat('{0:+}'.format(ele))
        value += x ** (lens-1-idx) * ele
        output = output.rstrip()
        output = output.replace('x^1', 'x')
        output = output.replace('1*x', 'x')
    return output + ' with x = {}'.format(x) + ' the value is '+ str(value)



pol_list = [9, 1, 60, 77]
x = -89
'For 9*x^3 + 1*x^2 + 60*x + 77 with x = -89 the value is -6342063'
'For 9*x^3 + x^2 + 60*x + 77 with x = -89 the value is -6342063'

print(calc_poly(pol_list, x))

import unittest


class MyTest(unittest.TestCase):

    # def setUp(self):
    #     self.assertEqual(1, 2)

    def assert_equals(self, left, right, msg='error'):
        try:
            self.assertEqual(left, right)
            print('haha')
        except Exception:
            print('-'*80)
            print(left)
            print(right)

test = MyTest()
pol_list = [6, 3, 5, -4]
x = 4
test.assert_equals(calc_poly(pol_list, x), "For 6*x^3 + 3*x^2 + 5*x - 4 with x = 4 the value is 448")
print('haha')
pol_list = [2, 0, 5, -6, 4, 0]
x = 2
test.assert_equals(calc_poly(pol_list, x), "For 2*x^5 + 5*x^3 - 6*x^2 + 4*x with x = 2 the value is 88")


plist = [1, 35, 36]
x = 97
test.assert_equals(calc_poly(plist, x), 'For x^2 + 35*x + 36 with x = 97 the value is 12840')

