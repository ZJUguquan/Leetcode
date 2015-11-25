def triangular_range(start, stop):
    result = {i: i * (i + 1) // 2 for i in range(1, int(stop * 2 ** .5) + 1)
              if i * (i + 1) // 2 >= start and i * (i + 1) // 2 <= stop}
    return result


def remove(text, what):
    result = ''

    for i in text:
        if i in what and what[i] > 0:
            what[i] -= 1
        else:
            result += i
    return result


# simpler
#

def remove(text, what):
    for char in what:
        text = text.replace(char,'',what[char])
    return text