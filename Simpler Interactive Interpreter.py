

import re
import operator


def oye(msg=None):
    print msg
    print '*' * 76

oye()

# http://www.codewars.com/kata/53005a7b26d12be55c000243/train/python


def tokenize(expression):
    import re
    if expression == "":
        return []

    regex = re.compile(
        "\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


operators = {
    '+': [operator.add, 2],
    '-': [operator.sub, 2],
    '*': [operator.mul, 3],
    '/': [operator.div, 3],
    '^': [operator.pow, 3],
    '%': [operator.mod, 3],
    '_': [lambda x: -x, 1],
}


class Interpreter:

    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        stack = []
        tokens = tokenize(expression)
        if len(tokens) < 1:
            return ''

        if len(tokens) == 1:
            try:
                return int(self.vars[tokens[0]])
            except Exception as e:
                raise KeyError(
                    'ERROR: Invalid identifier. \
                     No variable with name {} was found.'.format(tokens[0]))

        if len(tokens) == 3 and '=' in tokens:
            left, op, right = tuple(tokens)
            self.vars[left] = int(right)

        for idx, token in enumerate(tokens):
            if token in operators:   # +-*/
                if operator[token][1] == 2:  # + -
                    return operators[token][0](stack.pop(-1),
                        self.input(' '.join(tokens[idx + 1:])))
                elif operator[token][1] == 3:  # * /
                    return self.input(str(operator[token][0](int(stack.pop(-1)), int(tokens.pop(0)) )) + ' ' + ' '.join(tokens[idx + 2:]))
            if token not in operator:
                if token in self.vars:
                    stack.append(self.vars[token])
                else:
                    try:
                        token = int(token)
                        stack.append(token)
                    except Exception as e:
                        raise KeyError(
                            'ERROR: Invalid identifier. \
                             No variable with name {} was found.'.format(tokens[0]))




interpreter = Interpreter()
i = interpreter.input

print i("1 + 1")
oye()
print i("2 - 1")
print i("2 * 3")
print i("8 / 4")
print i("7 % 4")

oye('# Variables')
print i("x = 1")
print i('x')
print i('x + 3')
# test.assert_equals(interpreter.input("x"), 1)
# test.assert_equals(interpreter.input("x + 3"), 4)
# test.expect_error("input: 'y'", lambda : interpreter.input("y"))
        '''
        Complex Expression Evaluation
Should handle multiple operations
input: '4 + 2 * 3': None should equal 10
Should reject invalid input
input: '1 2'
input: '1two'
        '''