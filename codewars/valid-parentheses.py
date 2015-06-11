def valid_parentheses(string):
    print string

    st = []
    for ch in string:
        if ch in ('(',):
            st.append(ch)
        elif ch in (')'):
            if len(st) < 1 or st[-1] != '(':
                return False
            else:
                if st[-1] == '(':
                    st.pop()

    return len(st) < 1



class MyTest(object):

    def assert_equals(self, c1, c2, msg='-----'):
        if c1 == c2:
            print 'Test passssssssssssssssssssssssssssssssssssssss'
        else:
            print 'EEEEEEEEEEEEEEEEEEE' + msg

Test = MyTest()

Test.assert_equals(valid_parentheses("  ("), False)
Test.assert_equals(valid_parentheses(")test"), False)
Test.assert_equals(valid_parentheses(""), True)
Test.assert_equals(valid_parentheses("hi())("), False)
Test.assert_equals(valid_parentheses("hi(hi)()"), True)
