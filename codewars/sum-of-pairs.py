
def sum_pairs(list, sum):
  s = set()
  for v in list:
    if (sum - v) in s:
      return [sum - v, v]
    s.add(v)


def sum_pairs(alist, sum):
    result = []
    for elem in alist[::-1]:
        if sum - elem in alist[idx + 1:]:
            result.append([elem, sum])
    return result.pop() if len(result) > 0 else None


ls = [[1, 4, 8, 7, 3, 15],
      [1, -2, 3, 0, -6, 1],
      [20, -13, 40], [1, 2, 3, 4, 1, 0],
      [10, 5, 2, 3, 7, 5], [4, -2, 3, 3, 4], [0, 2, 0], [5, 9, 13, -3]
      ]
sums = [8, -6, -7, 2, 10, 8, 0, 10]
print('test ... test')
for idx, tlist in enumerate(ls):
    print(sum_pairs(tlist, sums[idx]), '---', sums[idx])
