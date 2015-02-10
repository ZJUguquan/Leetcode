bin = '01'
oct = '01234567'
dec = '0123456789'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



def convert(input, source, target):
    if source == target or len(input) < 1:
        return input
    total = 0
    for idx, cher in enumerate(input):
        # print(cher, source.find(cher))
        total += len(source) ** (len(input)-1-idx) * source.find(cher)
    if total < len(target):
        return target[total]
    result = []
    # print(total)
    while total > 0:
        total, residual = divmod(total, len(target))
        result.append(target[residual])
    return ''.join(result[::-1])


# print(convert('15', dec, bin)) # done
print(convert('hello', allow, hex))
print(convert('27', dec, allow))
