
def unique(_list):
    length = len(_list)
    if set(_list) == set(range(1, length + 1)):
        return True
    return False


class Sudoku(object):

    def __init__(self, soduku):
        self.soduku = soduku
        print self.soduku

    def is_valid(self):
        rows = len(self.soduku)
        if (rows == 1 and self.soduku[0][0] != 1):
            return False
        if type(self.soduku[0][0]) == type(True): return False
        # row check

        for row in self.soduku:
            if not unique(row):
                return False

        # column check
        for col in range(rows):
            if not unique([self.soduku[row][col] for row in range(rows)]):
                return False

        # Little Square
        little_square_length = int(rows**.5)
        for i in range(0, rows, little_square_length):
            for j in range(0, rows, little_square_length):
                temp = [self.soduku[i + row][j + col]
                        for row in range(little_square_length)
                        for col in range(little_square_length)
                        ]
                if not unique(temp):
                    return False

        return True
test = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 1, 5, 6, 4, 8, 9, 7], [3, 1, 2, 6, 4, 5, 9, 7, 8], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 4, 8, 9, 7, 2, 3, 1], [6, 4, 5, 9, 7, 8, 3, 1, 2], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 7, 2, 3, 1, 5, 6, 4], [9, 7, 8, 3, 1, 2, 6, 4, 5]]

soduku = Sudoku(test)
print soduku.is_valid()
print type(True)

# test = [
#     [0, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],

#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],

#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ]
# rows, little_square_length = 9, 3
# for i in range(0, rows, little_square_length):
#     for j in range(0, rows, little_square_length):
#         temp = [test[i + row][j + col]
#                 for row in range(little_square_length)
#                 for col in range(little_square_length)
#                 ]
#         print temp