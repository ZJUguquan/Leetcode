def to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '': 0}
    output = []
    opstack = ['']
    for idx, c in enumerate(infix):
        print(idx,'\t', c, output, opstack)
        if c.isdigit() or c == '(':
            output.append(c)
        elif c == ')':
            print(c, output, opstack)
            popped = opstack.pop()
            while popped != '(' and len(opstack) > 0:
                output.append(popped)
                popped = opstack.pop()

        else:
            while precedence[c] <= precedence.get(opstack[-1], 0) and c != '^':
                output.append(opstack.pop())
            opstack.append(c)
    output.extend(reversed(opstack))
    return ''.join([c for c in output if c != '('])

infix = '2+7*5'
infix = '3*3/(7+1)' # 33*71+/
# infix = '(7+1)'
print(to_postfix(infix))
