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


from operator import itemgetter
from math import ceil, floor

def meters(x=1):
	
    x_len = len(str(x))
    unit = [1000**i for i in range(9)]
    three_delimiter = { 3*i:i for i in range(9)}
    metrix = ['', 'k', 'M', 'G','T', 'P', 'E', 'Z', 'Y']

    # for idx, lens in three_delimiter[::-1]:
    for lens, _ in (sorted(three_delimiter.items(), key=lambda x: x[0], reverse=True)):
    	if x_len > lens:
    		front_part = x / float(1000 ** _)
    		if ceil(front_part) == floor(front_part):
    			front_part = int(front_part)
    		unit_part = metrix[_] + 'm'
    		return str(front_part) + unit_part 

i = 9*10**23
i = 12300000
i = 9000000000000
print(meters(i))