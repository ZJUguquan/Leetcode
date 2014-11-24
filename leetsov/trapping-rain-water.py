
'Trapping-Rain-Water'
"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6."""


# class Solution:
#     # @param A, a list of integers
#     # @return an integer
def trap(A):
    if len(A) <= 2:
        return 0
    elif len(A) == 3:
        if A[1] >= min(A[0], A[-1]):
            return 0
        else:
            return min(A[0], A[-1]) - A[1]
    area = 0
    start = 0
    for i in range(1, len(A)) :
        if A[i] < A[start]:
            pass
        elif A[i] == A[start]:
            start = i
        else: # start >
            height_top = A[i]
            left_height = max(A[start:i])
            left_area = sum([left_height-x for x in A[start:i] ])
            right_start = i
            if i < len(A) - 2:
                right_start = i + 1
                while A[right_start] <= left_height:
                    right_start += 1
            right_area = sum([left_height-x for x in A[i+1:right_start] ] )
            i = right_start
            area = area + left_area + right_area
            start = i
    return area

def trap(A):
    i, res = 0, 0; n = len(A)
    if n <= 2: return 0
    ltr = [0 for x in range(n)]
    rtl = [0 for x in range(n)]
    ltr[0] = A[0]
    for i in range(1, n):
        ltr[i] = max(ltr[i-1], A[i] )
    rtl[n-1] = A[n-1]
    for i in range(n-2, -1, -1):
        rtl[i] = max(rtl[i+1], A[i])
    res = sum([min(ltr[i], rtl[i]) - A[i] for i in range(n)])
    return res



A = [4,2,3]
A = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(A))
"""class Solution {
        vector<int> ltr(n, 0), rtl(n, 0);
        for(i = 1, ltr[0] = a[0]; i < n; i++)
            ltr[i] = max(ltr[i-1], a[i]);
        for(i = n - 2, rtl[n-1] = a[n-1]; i >= 0; i--)
            rtl[i] = max(rtl[i+1], a[i]);
        for(i = 0; i < n; i++)
            res += min(ltr[i], rtl[i]) - a[i];
        return res;
    }"""