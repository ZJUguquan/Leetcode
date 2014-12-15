def solution(s):
    m = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5,'I':1}
    s = s.upper()
    stack = [0]
    # reversed
    for c in s[::-1]:
        if m[c] >= stack[-1]:
            stack.append(m[c])
        else:
            v = stack.pop()
            stack.append(v-m[c])
    return sum(stack)


print(solution('XXI'))