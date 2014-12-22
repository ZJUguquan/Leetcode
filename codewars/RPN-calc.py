def calc(expr):
    # empty string
    if expr == "":
        return 0
    # 二元
    first, second, operator = expr.split()
    first, second = float()
    # return 0

print(calc(''))
print(calc('3 5 +'))
