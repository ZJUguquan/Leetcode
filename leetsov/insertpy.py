a = [1,3,5,6,10]
target = 9
b = a[-1]
while b > target:
    a.pop()
    b = a[-1]
if a[-1] < target:
    a.append(target)
    print len(a)



print a


a = [1,3,5,6,10]
target = 9
a = [x - target for x in a]
while a[-1] > 0:
    a.pop()
print len(a)

"****************************************************************************"
"Accept"

def searchInsert(A, target):
    if A[0] > target or A == []:
        return 0
    while len(A) > 0 and A[-1] >= target:
        #print A
        A.remove(A[-1])
    A.append(target)
    return A.index(target)

print 'test data'
print searchInsert([1,3,5,6], 5)
print searchInsert([1,3,5,6], 2)
print searchInsert([1,3,5,6], 7)
print searchInsert([1,3,5,8], 0)


# print [1,3,5,8].remove(8)
# A = [1,3,5,8]
# while A[-1] > 2:
#     # last = A[-1]
#     A.remove(A[-1])

# print A