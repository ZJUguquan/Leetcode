def midpoint_sum(ints):
    if len(ints) < 2:
        return None
    left, right = ints[0], 0
    left_pointer, right_pointer = 1, len(ints) - 1
    while left != right or right_pointer - left_pointer > 0:
        #print(left, right , left_pointer, right_pointer)

        if left > right:
            right += ints[right_pointer]
            right_pointer -= 1
        elif right > left:
            left += ints[left_pointer]
            left_pointer += 1
        elif left == right:
            if ints[left_pointer] == 0:
                left_pointer += 1
            elif ints[right_pointer] == 0:
                right_pointer -= 1
        if left == right and left_pointer == right_pointer:
            return left_pointer
    return None

ints = [4, 1, 7, 9, 3, 9]
# ints = [ 1, 0 ,0]
# ints = [9,0,1,2,3,4]
print(midpoint_sum(ints))
