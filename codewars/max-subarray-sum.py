def maxSequence(arr):
    if arr == [] or max(arr) <=0:
        return []
    # postive existed.
    max_so_far, max_ending_here = 0, 0
    curr = []
    for i in arr:
        old_max_sofar = max_so_far
        old_max_end = max_ending_here
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
            curr = []
        if max_so_far <= max_ending_here:
            max_so_far = max_ending_here
        if max_so_far >= old_max_sofar:
            curr.append(i)
        # if max_ending_here > 0:
        #     curr.append(i)
        print(i,'\t\t', max_so_far, max_ending_here)

    return max_so_far, curr


# wiki: http://en.wikipedia.org/wiki/Maximum_subarray_problem
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

'''

    # for x in A:
    #     max_ending_here = max(0, max_ending_here + x)
    #     max_so_far = max(max_so_far, max_ending_here)
'''
# http://ideone.com/bcMB3H


        # nonlocal end_index



def maxSequence(A):
    if A == [] or max(A) <= 0:
        return 0
    start_index, end_index = 0, 0

    overAllMax = A[0]
    currMax = A[0]
    for i in range(1, len(A)):
        if currMax + A[i] <= 0:
            start_index = i
        if A[i] > currMax + A[i]:
            currMax = A[i]
        else:
            currMax = currMax + A[i]

        if currMax > overAllMax:
            end_index = i
            overAllMax = currMax
        overAllMax = max(overAllMax, currMax)

    return A[start_index:end_index] #, overAllMax,


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [2, -1, 2, 3, 4, -5]
print(max_subarray(arr))