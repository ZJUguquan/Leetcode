

import unittest

def shorten(string, length, glue='...'):
    print string, length, glue
    lens = len(string)
    if lens <= length:
        return string

    if len(glue) + 2 > length:
        return string[:length]

    gaps = length - len(glue)
    left = gaps // 2
    right = length - left - len(glue)
    return string[:left] + glue + string[-right:]






class MyTest(object):

    def assertEqual(self, left, right, msg=None):

        if left != right:
            print left, right
            print str(msg)
        print '='* 50


test = MyTest()
if __name__ == '__main__':

    sentence = "The quick brown fox jumps over the lazy dog"
    res = shorten(sentence, 27)

    test.assertEqual(len(res), 27, 'Length is not 27')
    test.assertEqual(res, 'The quick br...the lazy dog', 'result does not match')

    res2 = shorten(sentence, 27, '----')

    test.assertEqual(len(res2), 27, 'Length is not 27')
    test.assertEqual(
        res2, 'The quick b----the lazy dog', 'result does not match')
