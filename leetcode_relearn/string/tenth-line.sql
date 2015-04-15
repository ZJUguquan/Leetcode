fcontent = '''
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
'''

i = 0
for row in [x for x in fcontent.split('\n') if len(x) > 0]:
    i += 1
    if i == 10:
        print(row)


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        #n =  11
        b = bin(n)[2:]
        import string
        return string.zfill(b, 32).count('1')