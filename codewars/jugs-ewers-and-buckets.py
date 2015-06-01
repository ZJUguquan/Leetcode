# coding: utf-8


########################################################################


class Test(object):
    def assert_equals(self, left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
test = Test()


def how_many_moves(containers, required, max_moves):
    curr_state = dict(zip(containers, [0]*len(containers)))
    if max_moves < 0:
        return -1
    if required in curr_state:
        curr_state[required] = required
        max_moves -= 1
        return 1



print how_many_moves([2, 3, 7, 19], 11, 10)

# test.assert_equals(how_many_moves([2, 3, 7, 19], 11, 10), 5)
# test.assert_equals(how_many_moves([2, 3, 7, 19], 11, 4), -1)