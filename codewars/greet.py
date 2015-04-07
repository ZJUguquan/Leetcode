def greet(name):
    if name == "Johnny":
        return 'Hello, my love!'
    return 'Hello, %s!' % name


print(greet('sam'))


from math import sqrt
from math import floor
def decompo(n):
    if n == 0:
        return None
    if n == 1:
        return [1]
    max_number = int(floor(sqrt(n)))
    if n == max_number ** 2:
        max_number -= 1
    while (n - max_number**2) > 0 :
        if decompo(n - max_number**2) is not None:
            return decompo(n - max_number**2) +[max_number]
        max_number -= 1
        if max_number == 1:
            break
    return None

# print(decompo(104))

def decompose(n):
    return decompo(n*n)


print(decompose(5))
print(decompo(25))