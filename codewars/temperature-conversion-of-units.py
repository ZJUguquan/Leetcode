'''
http://www.codewars.com/kata/54ce9497975ca65e1a0008c6/train/python
0202  倒数第2个 text 没过 不知道什么问题.
possible scale inputs:
    "C"  for Celsius
    "F"  for Fahrenheit
    "K"  for Kelvin
    "R"  for Rankine
    "De" for Delisie
    "N"  for Newton
    "Re" for Réaumur
    "Ro" for Rømer

convert_temp(   100, "C",  "F") # => 212
convert_temp(    40, "Re", "C") # => 50
convert_temp(    60, "De", "F") # => 140
convert_temp(373.15, "K",  "N") # => 33
convert_temp(   666, "K",  "K") # => 666
'''

int2 = lambda x: int(round(x, 0))

def other2c(temp, from_scale):
    func_dict = {
        'C': lambda x: x,
        'K': lambda x: int2(x - 273.15),
        'F': lambda x: int2((x - 32) * 5 / 9),
        'R': lambda x: int2((x - 491.67) * 5 / 9),
        'De': lambda x: int2(100 - x * 2 / 3),
        'N': lambda x: int2(x * 100 / 33),
        'Re': lambda x: int2(x * 5 / 4),
        'Ro': lambda x: int2((x - 7.5) * 40 / 21)
    }
    return func_dict[from_scale](temp)


def c2other(temp, to_scale):
    func_dict = {
        'C': lambda x: x,
        'K': lambda x: int2(x + 273.15),
        'F': lambda x: int2(x * 9 / 5 + 32),
        'R': lambda x: int2((x + 273.15) * 9 / 5),
        'De': lambda x: int2((100 - x) * 3 / 2),
        'N': lambda x: int2(x * 33 / 100),
        'Re': lambda x: int2(x * 4 / 5),
        'Ro': lambda x: int2(x * 21 / 40 + 7.5)
    }
    return func_dict[to_scale](temp)


def convert_temp(temp, from_scale, to_scale):
    if from_scale == to_scale:
        return temp
    nowc = other2c(temp, from_scale)
    c2res = c2other(nowc, to_scale)
    return c2res

print(convert_temp(100, 'C', 'F'))
print(convert_temp(40, 'Re', 'C'))
print(convert_temp(60, 'De', 'F'))
print(convert_temp(373.15, 'K', 'N'))
print(convert_temp(666, 'K', 'K'))
