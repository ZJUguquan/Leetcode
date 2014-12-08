def encryptor(key, message):
    import string
    res = ''
    for e in message:
        if e in string.ascii_letters:
            res += chr(ord(e) + key)
        else :
            res += e
    return res
    # return ''.join([ chr(ord(e) + key)  for e in message if e in  ])
    #Program me!

print(encryptor(1, 'Caesar Cipher'))


import string

def encryptor(key, message):
    transtab = string.maketrans(
        string.ascii_letters,
        (string.ascii_lowercase * 2)[key%26:key%26+26] + (string.ascii_uppercase * 2)[key%26:key%26+26])
    return message.translate(transtab)


print(-1%26)