
# valid number

is_number = lambda x: type(x) in (int, float) or all([i in \
    '1234567890.' for i in str(x) ])


def pivot(dataframe, col):
    print dataframe, col
    group = set([dataframe[r][col] for r in range(len(dataframe))])

    from collections import OrderedDict
    output = OrderedDict()

    for row in dataframe:
        if row[col] not in output:
            output[row[col]] = [0 for _ in range(len(row))]

        for idx, ele in enumerate(row):
            if idx == col:
                output[ele][idx] = ele
            if idx != col:
                if not is_number(row[idx]):
                    output[row[col]][idx] = '-'
                else:
                    output[row[col]][idx] += float(row[idx])
    group = sorted(group)
    return [output[k] for k in group]
report = [
      ["Item 1", "Man", "2500", "500", "Yellow"],
      ["Item 2", "Woman", "42", "8.4", "Blue"],
      ["Item 3", "Woman", "56", "11.2", "Purple"],
      ["Item 4", "Woman", "11", "2.2", "Yellow"],
      ["Item 5", "Man", "3600", "720", "Red"],
      ["Item 6", "Woman", "32", "6.4", "Red"],
      ["Item 7", "Man", "6700", "1340", "Yellow"],
      ["Item 8", "Woman", "25", "5", "Green"]
]



[['-', 'Black', 4870.0], ['-', 'Black', 4870.0], ['-', 'Red', 69.0], ['-', 'Red', 69.0]] should equal
[['-', 'Black', 4870.0], ['-', 'Red', 69.0]]
1 Passed


from pprint import pprint
pprint(pivot(report, 1))




## Testcase
#
#




report = [
["Item 1", "Black", "123"],
["Item 2", "Red", "34"],
["Item 3", "Black", "4747"],
["Item 4", "Red", "35"]
]

pprint(pivot(report, 0))

                   #[['Item 1', '-', 123.0], ['Item 2', '-', 34.0], ['Item 3', '-', 4747.0], ['Item 4', '-', 35.0]])

pprint(pivot(report, 1))
                  # [['-', 'Black', 4870.0], ['-', 'Red', 69.0]])



report = [['Item 1', 'Man', '2500', '500', 'Yellow'], ['Item 2', 'Woman', '42', '8.4', 'Blue'], ['Item 3', 'Woman', '56', '11.2', 'Purple'], ['Item 4', 'Woman', '11', '2.2', 'Yellow'], ['Item 5', 'Man', '3600', '720', 'Red'], ['Item 6', 'Woman', '32', '6.4', 'Red'], ['Item 7', 'Man', '6700', '1340', 'Yellow'], ['Item 8', 'Woman', '25', '5', 'Green']]

pprint(pivot(report, 4))

[['-', '-', 9211.0, 1842.2, 'Yellow'],
 ['-', '-', 42.0, 8.4, 'Blue'],
 ['-', '-', 56.0, 11.2, 'Purple'],
 ['-', '-', 3632.0, 726.4, 'Red'],
 ['-', '-', 25.0, 5.0, 'Green']]

#[['-', '-', 42.0, 8.4, 'Blue'],
#['-', '-', 25.0, 5.0, 'Green'],
#['-', '-', 56.0, 11.2, 'Purple'],
#['-', '-', 3632.0, 726.4, 'Red'],
#['-', '-', 9211.0, 1842.2, 'Yellow']]

