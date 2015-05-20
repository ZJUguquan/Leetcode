def diamond(n):
    if n % 2 == 0:
        return None
    expected = ''
    loop = range(1, n + 2, 2) + range(n - 2, 0, -2)
    for i in loop:
        expected += ('*' * i).center(n).rstrip() + '\n'

    return expected if len(expected) > 0 else None