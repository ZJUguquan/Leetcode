def char_concat(word):
    arr = list(word)
    print(arr)
    result = []
    for i in range(len(arr)):
        result.append(arr[i] + arr[-i - 1] + str(i))
    return " ".join(result)

print(char_concat("abc def"))