
# http://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
def tickets(people):
    from collections import defaultdict
    my_have = defaultdict(int)
    while people:
        give_money = people.pop(0)
        my_have[str(give_money)] += 1
        if give_money == 25:
            continue
        elif give_money > 25:
            if my_have['25'] == 0:
                return 'NO'
            if give_money == 50:
                my_have['25'] -= 1

            if give_money == 100:
                if my_have['50'] > 0:
                    my_have['50'] -= 1
                    my_have['25'] -= 1
                elif my_have['25'] >= 3:
                    my_have['25'] -= 3
                else:
                    return 'NO'
    return 'YES'

_list = [25, 25, 25, 25, 50, 100]
_list = []
print(tickets(_list))

