def to_postfix(infix):
    expr = list(infix)
    import string
    buffer = ''
    result = ''
    lower_operator = ['+', '-']
    digits_buffer = []
    lower_buffer = []
    higher_operator = [ '*', '^','/']
    higher_buffer = []
    for idx, chr in enumerate(infix):
        print(idx, buffer)
        if buffer == '' or chr in ['(', ')']:
            buffer += chr
            continue
        if chr in string.digits or chr:
            buffer += chr
            continue
        if ')' in buffer:
            result += (buffer[1]+buffer[3]+buffer[2])
            buffer = ''
        if len(buffer)>=3 and '(' not in buffer and (buffer.count('*') or buffer.count('/') or buffer.count('^')):
            buffer = ' '+buffer
            result += (buffer[1]+buffer[3]+buffer[2])
            buffer = ''
    return result

infix = '3*3/(7+1)'

# print(eval(infix))
print(to_postfix(infix))

# import operator

# ARITHMETIC_OPERATORS = {
#     '+':  operator.add, '-':  operator.sub,
#     '*':  operator.mul, '/':  operator.div,
#     '^': operator.pow
# }

def parse_rpn(expression):
    stack = []
    buffer = []
    for val in enumerate(expression):
        if val in ['+', '-', '*', '/']:
            op1 = stack.pop()
            po2 = stack.pop()
# def postfix(expression, operators=ARITHMETIC_OPERATORS):
#     stack = []
#     for val in expression.split():
#         if val in operators:
#             f = operators[val]
#             stack[-2:] = [f(*stack[-2:])]
#         else:
#             stack.append(int(val))
#     return stack.pop()

# print(postfix(infix))



# # RPB表达式 解析
# def parse_rpn(expression):
#   """ Evaluate a reverse polish notation """

#   stack = []

#   for val in expression.split(' '):
#       if val in ['-', '+', '*', '/']:
#           op1 = stack.pop()
#           op2 = stack.pop()
#           if val=='-': result = op2 - op1
#           if val=='+': result = op2 + op1
#           if val=='*': result = op2 * op1
#           if val=='/': result = op2 / op1
#           stack.append(result)
#       else:
#           stack.append(float(val))

#   return stack.pop()


# # The main program to try parse_rpn()
# if __name__ == '__main__':

#   expression = '10 3 5 + *'
#   result = parse_rpn(expression)
#   print result

#   expression = '3 5 + 10 *'
#   result = parse_rpn(expression)
#   print result