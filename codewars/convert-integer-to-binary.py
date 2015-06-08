


def to_binary(n):
    if n >= 0:
        return bin(n)[2:]
    else:
        a = '11111111111111111111111111111111'
        return bin(int(a, 2) + n + 1)[2:]

print to_binary(-3)


# # -3 '11111111111111111111111111111101
# a = '11111111111111111111111111111111'

# b = int(a, 2)
# print b
# print (bin(b))