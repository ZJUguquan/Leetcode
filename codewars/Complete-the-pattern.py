def pattern(n):
    # 2
    return '\n'.join([''.join([str(i) for i in range(n, end - 1, -1)]) for end in range(1, n + 1)])


def pattern(n):
    # 1
    return '\n'.join([str(i) * i for i in range(1, n + 1)])
########################################################################


def pattern(n):
    # 6 odd ladder
    return '\n'.join([str(i) * i for i in range(1, n + 1) if i % 2 == 1])


def pattern(n):
    # 3
    return '\n'.join([''.join([str(i) for i in range(n, end - 1, -1)]) for end in range(n, 0, -1)])


def pattern(n):
    # 4
    return '\n'.join([''.join([str(i) for i in range(start, n + 1, 1)]) for start in range(1, n + 1, 1)])
print repr(pattern(5))


def pattern(n):
    lst = range(1, n + 2)
    return '\n'.join([''.join(map(str, lst[i:-1] + lst[0:i])) for i in range(n)])

print pattern(9)



#Testing for 21
def pattern(n):
    lst = map(lambda x: str(x)[-1], range(1, n + 1))
    output = ''

    for i in range(n):
        output += ''.join(lst[:i] + lst[i-n::-1]).center(2*n-1)
        output += '\n'
    return output.strip('\n')