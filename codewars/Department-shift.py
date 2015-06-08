def month_has_day(mmyyyy):
    import re
    mmyyyy = re.sub(r'\D', '', mmyyyy)
    if len(mmyyyy) != 6:
        raise ValueError('date of month valid')
    month = int(mmyyyy[:2])
    year = int(mmyyyy [3:])
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:
        if year % 4 != 0:
            return 28
        else:
            if year % 100 != 0:
                return 29
            else:
                if year % 400 != 0:
                    return 28
                return 29

print month_has_day('02/2000')

def schedule(employees, month, n):
    '''
    1. one employee cannot have tow consecutive shifts
    2. n people at work each day
    3. workload is equal or differs from other minimallly(1 shift)
    4. if no solution returen None.

    result =
    schedule(['Smith', 'Jones', 'Gonzalez', 'White', 'Jackon', 'Taylor'], '022015', 3)
    print result
    Test.assert_equals(len(result), 28)
    result = schedule(['Smith', 'Jones', 'Gonzalez', 'White', 'Jackon', 'Taylor'], '022015', 4)
    print result
    Test.assert_equals(result, None)
    '''
    peoples = len(employees)
    if peoples < 2 * n:
        return None
    arrangement = []
    employees_table = employees * 31
    while len(arrangement) < month_has_day(month):
        shift = []
        for _ in range(n):
            shift.append(employees_table.pop(0))
        arrangement.append(shift)
    return arrangement


result = schedule(['Smith', 'Jones', 'Gonzalez', 'White', 'Jackon', 'Taylor'], '022015', 3)
should =    [['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson'],
    ['Smith', 'Jones', 'Gonzalez'],
    ['White', 'Jackson', 'Taylor'],
    ['Jones', 'Smith', 'Gonzalez'],
    ['Taylor', 'White', 'Jackson']]

# ls = []
# for es in result:
#     ls += es
# from collections import Counter
# c = Counter(ls)
# print c

# print  len(result)