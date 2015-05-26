def calc(expression):
    stack = []
    if expression == '':
        return 0
    for val in expression.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = float(stack.pop())
            op2 = float(stack.pop())
            if val == '-':
                result = op2 - op1
            if val == '+':
                result = op2 + op1
            if val == '*':
                result = op2 * op1
            if val == '/':
                result = op2 / op1
            stack.append(result)
        else:
            stack.append(val)
    return float(stack.pop())





print(calc(''))
print(calc('3 5 +'))
