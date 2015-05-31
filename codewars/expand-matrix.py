

def expand(maze, fill):
    n = len(maze)
    col = len(maze[0])
    expanded = [ [fill] * 2*n for i in range(n*2)]
    print len(expanded)
    for r in range(n/2, n/2 + n):
        for c in range(n/2, n/2+n):
            print r, c, r-n/2, c-n/2
            expanded[r][c] = maze[r-n/2][c-n/2]

    # do it
    return expanded

# def tester(m, fill, soln):
#     user = expand(m, fill)
#     if len(user) != len(soln) or len(user[0]) != len(soln):
#         print("your dimensions didn't match")
#         return False
#     for i, row in enumerate(user):
#         for j, ele in enumerate(row):
#             if ele != soln[i][j]:
#                 print("---FAILED---")
#                 print_mat(m)
#                 print("produced")
#                 print_mat(user)
#                 print("I wanted")
#                 print_mat(soln)
#                 print("------------")
#                 return False
#     return True

mat =  [[1, 1],[1, 1]]
correct_mat = [[0, 0, 0, 0],[0, 1, 1, 0],[0, 1, 1, 0],[0, 0, 0, 0]]
print expand(mat, 0)
# Test.expect(tester(mat, 0, correct_mat))