


from string import ascii_lowercase, ascii_uppercase


def moving_shift(string, shift):
    words = string
    lens = len(words)
    m, n = divmod(lens, 5)
    if n > 0:
        m +=1
    res = ['', '', '', '' ,'']
    chars = -1

    for idx, char in enumerate(words):
        chars += 1
        change=None
        if char in ascii_lowercase + ascii_uppercase:
            if char in ascii_lowercase:
                pos = ascii_lowercase.index(char)
                np = (pos + shift + chars) % 26
                change = ascii_lowercase[np]
            elif char in ascii_uppercase:
                pos = ascii_uppercase.index(char)
                np = (pos + shift + chars) % 26
                change = ascii_uppercase[np]
        else:
            change = char
        res[chars//m] += change
    return res

print '*' * 80

def demoving_shift(strings, shift):
    raw_string = ''
    coded_message = ''.join(strings)
    lens = len(coded_message)
    chars = -1
    for idx, char in enumerate(coded_message):
        chars +=1
        change=None
        if char in ascii_lowercase + ascii_uppercase:
            if char in ascii_lowercase:
                pos = ascii_lowercase.index(char)
                np = (pos - shift - chars) % 26
                change = ascii_lowercase[np]
            elif char in ascii_uppercase:
                pos = ascii_uppercase.index(char)
                np = (pos - shift - chars) % 26
                change = ascii_uppercase[np]
        else:
            change = char
        raw_string += change

    return raw_string

print moving_shift("I should have known that you would have a perfect answer for me!!!", 1)
# # test case
assert moving_shift("I should have known that you would have a perfect answer for me!!!", 1) == ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

de = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]

print demoving_shift(de, 1)