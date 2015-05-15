def isBalanced(s):
    level = 0
    for c in s:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        if level < 0:
            return False
    return level == 0



########################################################################

# Given a string which may include opening or closing round brackets,
# can you tell whether the string contains a balanced pair(s) of round brackets,
# that is there are no brackets which are either opened & not closed, or vice versa.
# Opening round brackets always have to come before closing bracket.
# test.assert_equals(isBalanced("hi)("),False)
# test.assert_equals(isBalanced("hi(hi)"),True)
# test.assert_equals(isBalanced("("),False)

def isBalanced(str):
    mapping = {'(': -1, ')':1}
    _stack = []
    for w in str:
        if w == ')':
            if len(_stack)>0 and _stack[-1] == '(':
                _stack.append(w)
            if _stack[-1] == ')'
        if (len(_stack) < 1 or _stack[-1] == ')' ) and w=='(':
            _stack.append(w)
    return len(_stack) > 0 and len(_stack) % 2 == 0

print isBalanced("hi)(")
print isBalanced("hi(hi)")
print isBalanced("((( ))))")
