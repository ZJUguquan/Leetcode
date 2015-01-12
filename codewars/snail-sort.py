'solved:'


def snail(array):
    result = []
    if len(array) == 0 or len(array[0]) == 0:
        return result
    size = len(array) - 1
    for x in range(size + 1):
        result.append(array[0][x])
    for x in range(1, size + 1):
        result.append(array[x][size])
    for x in range(size - 1, -1, -1):
        result.append(array[size][x])
    for x in range(size - 1, 0, -1):
        result.append(array[x][0])
    sub_array = []
    for x in range(1, size):
        row = []
        for y in range(1, size):
            row.append(array[x][y])
        sub_array.append(row)
    result += snail(sub_array)
    return result

##

import numpy as np


def snail(array):
    arr = np.array(array)

    if len(arr) < 2:
        return arr.flatten().tolist()

    tp = arr[0, :].tolist()
    rt = arr[1:, -1].tolist()
    bm = arr[-1:, :-1].flatten()[::-1].tolist()
    lt = arr[1:-1, 0][::-1].tolist()

    return tp + rt + bm + lt + snail(arr[1:-1, 1:-1])

##


def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


array = [[1, 2], [3, 5]]
# def spiral(n):
#     dx, dy = 0, -1
#     x, y = 0, 0
#     myarray = [ [None] * n for j in range(n)]
#     for i in range(n**2):
#         myarray[x][y] = i
#         nx, ny = x+dx, y+dy
#         if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
#             x, y = nx, ny
#         else:
#             dx, dy = -dy, dx
#             x, y = x+dx, y+dy
#     return myarray

# def printspiral(myarray):
#     n = range(len(myarray))
#     for y in n:
#         for x in n:
#             print("{}".format( myarray[x][y]), end = ' ')
#         print
from pprint import pprint
# pprint(spiral(5))
# printspiral(spiral(5))


def snail(array):

    n = len(array)
    res = []
    if n == 0:
        return []
    if n == 1:
        return array[0]
    levelNum = n // 2
    for level in range(levelNum):
        for i in range(level, n - level - 1):
            res.append(array[level][i])
        for i in range(level, n - level - 1):
            res.append(array[i][n - 1 - level])
        for i in range(n - level - 1, level, -1):
            res.append(array[n - 1 - level][i])
        for i in range(n - 1 - level, level, -1):
            res.append(array[i][level])
    if n % 2 == 1:
        for i in range(levelNum, n - levelNum):
            res.append(array[i][levelNum])
    return res
    # x, y = 0, 0
    # dx, dy = -1, 0
    # for i in range(n ** 2):
    #     if 0 <= x < n and 0 <= y < n:
    #         print(array[x][y], '-h', i)
    #     if abs(x) == abs(y) and x + y >= n:
    #         dx, dy = -dy, -dx
    #     elif (abs(x) == abs(y)):
    #         dx, dy = dy, -dx
    #     elif x + y == n - 1:
    #         dx, dy = dy, dx
    #     x, y = x + dx, y + dy
    #     print('当前方向', dx, dy, '当前index:', x, y)

print(snail(array))
