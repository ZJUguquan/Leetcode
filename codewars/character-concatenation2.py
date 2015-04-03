def char_concat(word):
    arr = list(word)
    mid = len(word) // 2
    result = ''
    for i in range(mid):
        result += arr[i]+arr[-(i+1)]+str(i+1)
    return result


print(char_concat('abcdef'))