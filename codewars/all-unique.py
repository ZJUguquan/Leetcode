def has_unique_chars(str):
    s = set()
    for i in str:
        i = ord(i)
        if i not in s:
            s.add(i)
        else:
            return False
    return True

s = 'abcde'
print(has_unique_chars(s))