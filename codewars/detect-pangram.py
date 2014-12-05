
'Detect Pangram'
import string

s = "The quick, brown fox jumps over the lazy dog!"
print(string.ascii_lowercase in s)


import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())