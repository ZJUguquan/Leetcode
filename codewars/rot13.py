

import string
def rot13(message):
    key = 13
    transtab = string.maketrans(
        string.ascii_letters,
        (string.ascii_lowercase * 2)[key%26:key%26+26] + (string.ascii_uppercase * 2)[key%26:key%26+26])
    return message.translate(transtab)


print string.letters
text = 'EBG13 rknzcyr.'
print rot13(text)