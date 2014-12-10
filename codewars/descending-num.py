def Descending_Order(num):
    #Bust a move right here
    return int(''.join(sorted([str(i) for i in str(num)], reverse=True)) )

print(Descending_Order(145263))


def dice(minimum, maximum):
    # 10 21 12 17 22 17 12 2 8 17 18 16 2 17 18 7 21 22 6 12 2 8 6 21 2 8 25 17 1 7 21 14 9 18 22 7 6 23 8 6 7 19 22 25 25 18 5
    from random import randint
    return randint(minimum, maximum)

print(dice(2,7))
