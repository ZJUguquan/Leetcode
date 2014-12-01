def run_length_encoding(s):
    res = []; copy = 0; pointer = s
    for idx, ch in enumerate(s):
        if idx == 0:
            pointer = s[idx]; copy = 1

        elif idx <= len(s) - 2:
            if s[idx] != s[idx-1]:
                res.append([copy, pointer])
                pointer = s[idx]
                copy =  1
            else:
                copy += 1
        elif idx == len(s) - 1:
            if s[idx] != s[idx-1]:
                res.append([copy, pointer])
                pointer = s[idx]
                res.append([1, s[idx]])
            else:
                res.append([copy+1, pointer])

    return res


def run_length_encoding(s):
    pairs = []
    for c in s:
        if pairs and pairs[-1][1] == c:
            pairs[-1][0] += 1
        else:
            pairs.append([1, c])
    return pairs

s = 'hello world'
# s = 'hello world!'
print(run_length_encoding(s))

'''test n o pass
[[1, 'h'], [1, 'e'], [2, 'l'], [2, 'o'], [2, ' '], [2, 'w'], [2, 'o'], [2, 'r'], [2, 'l'], [2, 'd'], [1, '!']] should equal [[1, 'h'], [1, 'e'], [2, 'l'], [1, 'o'], [1, ' '], [1, 'w'], [1, 'o'], [1, 'r'], [1, 'l'], [1, 'd'], [1, '!']]

'''