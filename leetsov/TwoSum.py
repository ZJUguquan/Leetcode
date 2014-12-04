class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index1, index2 = 0, 0
        for index1 in range(len(num)):
            for index2 in range(len(num)-1, index1, -1):
                if num[index1] + num[index2] == target:
                    return (index1+1, index2+1)

 # 'TLMI  Time Limit Exceeded'
def twoSum(num, target):
    index1, index2 = 0, 0
    for index1 in range(len(num)):
        for index2 in range(len(num)-1, index1, -1):
            if num[index1] + num[index2] == target:
                return (index1+1, index2+1)



'Find O(n) Solution'

#Key is the number and value is its index in the vector.
def twoSum(nums, target):
	hashT = {}
	result = []
	for i in range(len(nums)):
		numberToFind = target - nums[i]
		if numberToFind in hashT.keys():
			result.append(hashT[numberToFind] + 1)
			result.append(i + 1);
			return tuple(result)
		hashT[nums[i]] = i
		print(hashT)
	return tuple(result)


num = [2,7,11,15]; target = 9
# num = [3,2,4]; target = 6
print(twoSum(num, target))
