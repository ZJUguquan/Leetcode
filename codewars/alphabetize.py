# coding: utf-8




def sort_it(list_, n):
    #your code here
    return ', '.join(sorted(list_.split(', '), key=lambda x: x[n-1]))


def o(msg=None):
    print( ('*'*30+str(msg)+'*'*30).center(80))

class Test(object):
    @staticmethod
    def assert_equals(left, right, msg=None):
        if left == right:
            pass
        else:
            print('left\t: {l}'.format(l=left))
            print('right\t: {r}'.format(r=right))
        o(msg)





Test.assert_equals(sort_it('bill, bell, ball, bull', 2),'ball, bell, bill, bull' , 'Sort by the second letter')
Test.assert_equals(sort_it('cat, dog, eel, bee', 3),'bee, dog, eel, cat' , 'Sort by the third letter')