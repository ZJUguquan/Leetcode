def sum_pairs(list, sum):
    for idx, elem in enumerate(list):
        if sum - elem in list and elem != sum//2:
            return [elem, list[list.index(sum-elem)]]
    return None


list = [11, 3, 7, 5]
s = 10
list =  [10, 5, 2, 3, 7, 5] # [5, 9, 13, -3]
s = 10
print(sum_pairs(list, s))

