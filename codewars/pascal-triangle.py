def pascal(p):
    #your code here
    start = [1]
    result = [start]
    row = 1
    if p == 1:
        return result
    elif p == 2:
        return [[1], [1, 1]]
    result = [[1], [1, 1]]
    row = 3
    while row < p + 1:
        last_row = result[-1]
        newrow = [1, 1]
        for idx, element in enumerate(last_row):
            if idx < len(last_row) -1:
                newrow.insert(idx+1, element + last_row[idx+1])

        result.append(newrow)
        row += 1
    return result

from pprint import pprint

pprint(pascal(5))