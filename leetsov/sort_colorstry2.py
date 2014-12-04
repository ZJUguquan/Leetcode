class Solution:
# @param A a list of integers
# @return nothing, sort in place
def sortColors(self, A):
    red, blue = 0, len(A)-1
    i = 0
    while i <= blue:
        if A[i] == 0:
            if i > red:
                A[red] = 0
                A[i] = 1
            red += 1
        elif A[i] == 2:
            while blue > i and A[blue] == 2:
                blue -= 1
            if blue == i:
                break
            if A[blue] == 0:
                A[red] = 0
                if i > red:
                    A[i] = 1
                red += 1
            else:
                A[i] = 1
            A[blue] = 2
            blue -= 1
        i += 1