
def cubic(number):
    huns, tens, units = number // 100, number % 100 // 10, number % 10
    return huns ** 3 + tens ** 3 + units ** 3 == number


cubic = [0, 1, 153, 370, 371, 407]


def is_sum_of_cubes(s):
    import re
    cubic_pools = []
    tokens = re.findall('(\d{1,3})', s)
    for token in tokens:
        if int(token) in cubic:
            cubic_pools.append(int(token))

    if len(cubic_pools) < 1:
        return "Unlucky"
    cubic_pools.append(sum(cubic_pools))
    return ' '.join([str(i) for i in cubic_pools]) + ' Lucky'


s = "aqdf& 0 1 xyz 153 777.77117"
print is_sum_of_cubes(s)
