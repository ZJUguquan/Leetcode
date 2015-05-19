


def tetrahedron(n):
    if n == 1:
        return 1

    return (n*(n+1)*(3+2*n+1)) // 12
for i in [5, 11, 17, 47]:
    print(tetrahedron(i))