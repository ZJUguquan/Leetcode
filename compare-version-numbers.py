# # Compare two version numbers version1 and version1.
# # If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# # You may assume that the version strings are non-empty and contain only digits and the . character.
# # The . character does not represent a decimal point and is used to separate number sequences.
# # For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# # Here is an example of version numbers ordering:

# class Version(object):

#     def __init__(self, s):
#         self.stack = []
#         if '.' in str(s):
#             self.stack = [int(i) for i in str(s).split('.')]
#         else:
#             self.stack = [int(s)]
#     def compare(self, other):
#         short = min(len(self.stack), other.stack)
#         for i in range(short):
#             if self.stack[i] > other.stack[i]:
#                 return 1
#             if  self.stack[i] < other.stack[i]:
#                 return -1

#         # if (self.f, self.s) > (other.f, other.s):
#         #     return 1
#         # if (self.f, self.s) < (other.f, other.s):
#         #     return -1
#         return 0
#         # if self

# class Solution:
#     def compareVersion(self, version1, version2):
#         v1 = Version(version1)
#         v2 = Version(version2)
#         return v1.compare(v2)






class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        def removeTailZero(l):
            for i in xrange(len(l)-1,-1,-1):
                if int(l[i])!=0:
                    break
                del l[i]
        v1,v2 = version1.split("."),version2.split(".")
        removeTailZero(v1)
        removeTailZero(v2)
        for i in xrange(min(len(v1),len(v2))):
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v2[i])>int(v1[i]):
                return -1
        if len(v1)>len(v2): return 1
        elif len(v1)<len(v2): return -1
        else: return 0
s = Solution()
print(s.compareVersion(1, 1.0))
# 0.1 < 1.1 < 1.2 < 13.37
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# print(dir(1))
a = (3, 5)
b = (4, 10)
print(a>b)

print(dir(a))