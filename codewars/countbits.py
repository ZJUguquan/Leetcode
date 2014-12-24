def countBits(n):
    # print(bin(n))
    return bin(n).count('1')

print(countBits(1234))


li = [ 0,4,7,9,10]
for i in li:
    print(countBits(i))