def is4m(n):
    if not isinstance(n, int):
        return False
    while n % 4 == 0:
        n = n // 4
    if n == 1 or n == -1:
        return True
    return False


print(is4m(-16))

print(1 == True)

print(isinstance(True, int))

n = True
if n is not True and (n == 1 or n == -1 ):
        print(32)