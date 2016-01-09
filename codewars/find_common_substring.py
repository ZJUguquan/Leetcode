def substring_test(str1, str2):
    s1 = str1.lower()
    s2 = str2.lower()
    for idx, ch in enumerate(s1[:-1]):
        if ch not in s2: pass
        if ch + s1[idx+1] in s2:
            return True
    return False
