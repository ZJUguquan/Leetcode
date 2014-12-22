def cooking_time(eggs):
    if eggs == 0:
        return 0
    s, y = divmod(eggs, 8)
    return 5 * (s+1) if y > 0 else 5*s


test = [0, 5, 10, 16]
for i in test:
    print(cooking_time(i))