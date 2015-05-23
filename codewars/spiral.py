class Pointer(object):
    pass


def spiralize(size):
    if size == 1:
        spiral = [[1]]
    elif size == 2:
        spiral = [[1, 1], [0, 1]]
    elif size == 3:
        spiral = [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    return spiral