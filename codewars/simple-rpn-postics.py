def solve_postfix(expression):
    #your code here
    stack = []
    if expression == '':
        return 0
    for val in expression.split(' '):
        if val in ['-', '+', '*', '/', '^']:
            op1 = int(stack.pop())
            op2 = int(stack.pop())

            if val == '-':
                result = op2 - op1
            if val == '+':
                result = op2 + op1
            if val == '*':
                result = op2 * op1
            if val == '/':
                result = op2 / op1
            if val == '^':
                result = op2 ** op1
            stack.append(result)
        else:
            stack.append(val)
    return (stack.pop())