def mineLocation(field):
    # your code here
    for row in field:
        if max(row) == min(row):
            pass
        else:
            for c in row:
                if c > 0:
                    return [field.index(row), row.index(c)]


field = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
print(mineLocation(field))
