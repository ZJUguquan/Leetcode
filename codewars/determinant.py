
def determinant(matrix):
    rows = len(matrix)
    if rows == 1:
        return matrix[0][0]
    elif rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        M = 0
        for idx, ele in enumerate(matrix[0]):
            sub_ele = [row[:idx] + row[idx + 1:] for row in matrix[1:]]
            M += ele * (-1)**idx * determinant(sub_ele)
    return M


m1 = [[1, 3], [2, 5]]
m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]


print(determinant(m1))
print(determinant(m2))


for row in m2[1:]:
    print row
