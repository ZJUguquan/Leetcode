import re


def group_check(s):
    pat = "(\(\)|\[\]|\{\})"
    while re.search(pat, s):
        s = re.sub(pat, "", s)
    return len(s) < 1


def group_check(s):
    stack = []
    adict = {"(": ")", "[": "]", "{": "}"}
    for character in s:
        if stack == [] or character in adict:
            stack.append(character)
        top = stack[-1]
        if top in adict:
            if adict[top] == character:
                stack.pop()
    if stack == []:
        return True
    return False


from unittest import TestCase

Test = TestCase()

Test.assertEquals(group_check("()"), True)
Test.assertEquals(group_check("({"), False)
