array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]


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
    x, y = 0, 0
    dx, dy = -1, 0
    for i in range(n**2):
        if 0<=x <n and 0<=y <n:
            print(array[x][y], '-h', i)
        if abs(x) == abs(y) and x+y >n:
            dx, dy = -dy, dx
        elif (abs(x) == abs(y)):
            dx, dy = dy, -dx
        elif x+y == n-1:
            dx, dy = dy, dx
        x, y = x+dx, y + dy
        print('当前方向', dx, dy, '当前index:', x, y)

snail(array)