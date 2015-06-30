from string import maketrans
from string import ascii_lowercase, ascii_uppercase

def decode(string_):
    trans = maketrans(ascii_lowercase+ascii_uppercase, ascii_lowercase[::-1]+ascii_uppercase[::-1])
    if type(string_) != str:
        return "Input is not a string"
    return string_.translate(trans)