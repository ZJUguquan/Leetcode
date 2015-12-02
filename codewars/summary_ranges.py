

def summary_ranges(lst):
    output = []
    if not lst or lst != sorted(lst):
        return output
    left = lst[0]
    last = left
    while lst:
        popguy = lst.pop(0)

        if not lst:
            if popguy == last:
                if last > left:
                    output.append(str(left) + "->" + str(last))
                else:
                    output.append(str(left))
            elif popguy == (last + 1):
                output.append(str(left) + "->" + str(last + 1))
            else:
                output.append(str(left) + "->" + str(last))
                output.append(str(popguy))
        else:
            if popguy == last:
                pass
            elif popguy == (last + 1):
                last += 1
            else:
                if last > left:
                    output.append(str(left) + "->" + str(last))
                    left = last = popguy
                else:
                    output.append(str(left))
                    left = last = popguy

    return output



def summary_ranges(nums):
    if not nums:
        return []
    ranges = []
    first = nums[0]
    for current, previous in zip(nums[1:], nums[:-1]):
        if current - previous not in [0, 1]:
            ranges.append((first, previous))
            first = current
    ranges.append((first, nums[-1]))
    return ["{}->{}".format(a, b) if a!=b else str(a) for a, b in ranges]

print (summary_ranges([1, 2, 3, 4]))  # == ['1->4']
print summary_ranges([0, 1, 2, 5, 6, 9])  # == ["0->2", "5->6", "9"]
print summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7])  # == ["0->7"]
summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == [
    "0->7", "9->10"]
print summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9,
                      9, 10, 12])  # == ["-2", "0->7", "9->10", "12"]
print summary_ranges([1, 1, 1, 1, 1])  # == ['1']
print summary_ranges([2, -4, 1, 2, 6, -5, 5, -2, 5, -3, 7, -4, -3, 3, 4, 0, -4, 4, 6, 7, 8, 2, 9, 3, 4, 0, 1, 1, 2])
# It should work for random inputs too: ['2', '-4', '1->2', '6', '-5', '5', '-2', '5', '-3', '7', '-4->-3', '3->4', '0', '-4', '4', '6->8', '2', '9', '3->4', '0->2'] should equal []
#
#
# Testing for [2, -4, 1, 2, 6, -5, 5, -2, 5, -3, 7, -4, -3, 3, 4, 0, -4, 4, 6, 7, 8, 2, 9, 3, 4, 0, 1, 1, 2]
# It should work for random inputs too: ['2', '-4', '1->2', '6', '-5', '5', '-2', '5', '-3', '7', '-4->-3', '3->4', '0', '-4', '4', '6->8', '2', '9', '3->4', '0->2'] should equal []

