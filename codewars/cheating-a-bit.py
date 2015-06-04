# coding: utf-8

# url: http://www.codewars.com/kata/cheating-a-bit-dot-dot-dot/solutions?show-solutions=1
# remember: str contains binary data

def patch_data(str):
    pos = 0
    res = ''
    while pos < len(str):
        length = ord(str[pos + 0]) | (ord(str[pos + 1]) << 8) # parse the name length
        res += str[pos:pos + 2 + length] # copy the length + name
        res += "\xF4\x01" # 500 in 16-bit LE
        pos += 2 + length + 2 # advance the position
    return res




import binascii

ex = "\b\x00Domitius\x04\x00"

print type(ex)
print binascii.b2a_uu(ex)

########################################################################


class Test(object):
    def assert_equals(self, left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
test = Test()
