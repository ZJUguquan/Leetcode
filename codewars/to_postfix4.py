def to_postfix(infix):
    stack = []   # Handles operators.
    postfix = ''  # Return string.

    # Relative precedence of operators
    precedence = {'+': 1,
                  '-': 1,
                  '/': 2,
                  '*': 2,
                  '^': 3}

    # Iterate over infix string.
    for i in infix:
        if i in '+-*/^':
            # Operator found
            while (stack)  and precedence.setdefault(stack[-1], 0) >= precedence[i]:
                # Unload operators of high precedence than current character
                # and add to return string
                postfix += stack.pop()
            stack.append(i)
        elif i == '(':
            stack.append(i)
            # Parenthesis found.
        elif i == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            # Operand found. Add to output string.
            postfix += i

    # Dump the remainder of the stack into the return string.
    while stack:
        postfix += stack.pop()
    return postfix


infix = '3*3/(7+1)'
print(to_postfix(infix))
