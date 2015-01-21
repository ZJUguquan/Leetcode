a = 'indivisibility'
print(sorted(a))
print(sorted(set(a)))

def duplicate_count(s):
    return len (s) - len(dict.fromkeys(s))
