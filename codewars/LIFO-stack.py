class CWStack(object):

    def __str__(self):
        return "Stack of size: %s" % len(self._stack)

    def __init__(self):
        self._stack = []

    def push(self, element):
        self._stack.append(element)

    def isEmpty(self):
        return False if len(self._stack) > 0 else True

    def pop(self):
        return self._stack.pop()

    def top(self):
        if len(self._stack) > 0:
            return self._stack[-1]
        return None


def reverse_str(s, stack):
    for ch in s:
        stack.push(ch)
    rest = ''#.join(stack._stack[::-1])
    while not stack.isEmpty():
        rest += stack.pop()
    return rest

k = reverse_str('hello', CWStack())
print(k)