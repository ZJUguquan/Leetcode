bin='01'
oct='01234567'
dec='0123456789'
hex='0123456789abcdef'
allow='abcdefghijklmnopqrstuvwxyz'
allup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source=bin, target=dec):
    realN = 0
    J = len(source)
    for idx, i in enumerate(input):
        realN += list(source).index(i) * J ** (len(input) - 1 - idx)
    T = len(target)
    output = ''
    if realN < T:
        return target[realN]
    while realN > T:
        realN, n = divmod(realN, T)
        output += str(realN)
        if realN < T:
            output += target[n]
    return output




print(
convert("15", dec, bin), #should return "1111"
convert("15", dec, oct), #should return "17"
convert("1010", bin, dec), #should return "10"
convert("1010", bin, hex), #should return "a"
convert("0", dec, alpha), #should return "a"
convert("27", dec, allow), #should return "bb"
convert("hello", allow, hex) #should return "320048"

)