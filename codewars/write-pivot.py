

from collections import defaultdict
is_string = lambda s: any(map(str.isalpha, list(s)))



def pivot(two_dimensional_array, index_to_pivot, aggfunc=sum):
    groups = []

    lens = len(two_dimensional_array[0])
    agg_all = [defaultdict(float)] * lens
    string_indices = []
    row1 = two_dimensional_array[0]

    for idx, ele in enumerate(row1):
        if is_string(ele):
            string_indices.append(idx)




    for row in two_dimensional_array:
        for idx, ele in enumerate(row):
            if idx == index_to_pivot:
                continue
            elif idx in string_indices:
                continue
            else:
                agg_all[idx][row[index_to_pivot]] += row[idx]





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


tor = pivot(report, 1)

result = [
['-', 'Man', 12800.0, 2560.0, '-'],
['-', 'Woman', 166.0, 33.2, '-']
]



print "25.2".isdigit()
print float("25.2")
# print type(float('item'))


print any(map(str.isalpha, list('item 1')))