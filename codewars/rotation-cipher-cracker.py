import string


def caesar(message, key):
    transtab = string.maketrans(
        string.ascii_letters,
        (string.ascii_lowercase * 2)[key % 26:key % 26 + 26] + (string.ascii_uppercase * 2)[key % 26:key % 26 + 26])
    return message.translate(transtab)

# s = 'ymjxvznwwjqnxhzyj'
# s = 'lzwespnsdmwakafxafalq'
# c = 'max'


def decode(msg, contents):
    result = []
    for i in range(26):
        re = caesar(msg, i)
        if contents in re:
            result.append(re)
    return result

#print(decode(s, c))
