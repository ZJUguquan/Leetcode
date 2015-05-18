


def luck_check(string):
    mid = len(string) // 2
    if len(string) % 2 == 1:
        string = string[:mid] + string[mid+1:]

    return sum(map(int, string[:mid]) ) == sum(map(int, string[mid:]) )

print luck_check('683000')