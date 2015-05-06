# coding: utf-8

# def meters(x):
#     right_zeros = 0
#     for i in str(x)[::-1]:
#         if i == '0':
#             right_zeros += 1
#         else:
# 	        break


#     unit = [1, 1000**1, 1000**2, 1000**3, 1000**4, 1000**5, 1000**6, 1000**7, 1000**8]
#     metrix = ['', 'm', 'km', 'Mm', 'Gm','Tm', 'Pm', 'Em', 'Zm', 'Ym']

#     for idx, u in enumerate(unit):

#         if x < u:
#             if x % unit[idx-1] == 0 :
#                 return str(int(x//unit[idx-1])) + metrix[idx]
#             return str(x/float(unit[idx-1])) + metrix[idx]

#     return  str(x/unit[-1]) +'Ym'


# print meters(180 * 1000**3)

# test_set = [1, 123, 12300000, 9.1*1000**8]
# for t in test_set:
# 	print meters(t)


from math import ceil, floor


def trailing_zeros(longint):
    manipulandum = str(longint)
    return len(manipulandum) - len(manipulandum.rstrip('0'))


def meters(x=1):
    x = int(x)
    x_len = len(str(x))
    unit = [1000 ** i for i in range(9)]
    three_delimiter = {3 * i: i for i in range(9)}
    metrix = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']

    sthree= sorted(three_delimiter.items(), key=lambda x: x[0], reverse=True)
    for lens, index in sthree:
    	if x_len > lens:

            front_part = x / float(1000 ** index)
            unit_part = metrix[index] + 'm'
            quotient, reminder = divmod(x, 1000 ** index)
            if reminder == 0:
                return str(quotient) + unit_part
            else:
                return str(front_part) + unit_part





i = int(9.1*10**24)
i = 9000000000000000000000000
# i = 12300000
# i = 9000000000000000385875968
# i = 1
print(meters(i))


# 最终真的把弄郁闷了-- 我在这里显示9  测试时就是9.0


def meters(x):
    #your code here
    arr = ['','k','M','G','T','P','E','Z','Y']
    count=0

    while x>=1000 :
        x /=1000.00
        count+=1

    if int(x)==x:
        x=int(x)
    return str(x)+arr[count]+'m'