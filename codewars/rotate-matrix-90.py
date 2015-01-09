# modify and return the original matrix rotated 90 degrees clockwise in place

# www.codewars.com/kata/53fe3578d5679bf04900093f/train/python

def rotate_in_place(matrix):
    return [[row[i] for row in reversed(matrix)] for i in range(len(matrix))]