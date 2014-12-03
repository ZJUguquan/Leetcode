def count_change(money, coins, res=0):
    # your implementation here
    coins_sort = sorted( list(set(coins)))
    max_number = [money//i for i in coins_sort]
    if len(coins_sort) == 1:
        return res+1 if money % coins_sort[0] == 0 else res
    if money == 0:
        return 1
    # count the numbers of ways using max_coin

    if len(coins_sort) >= 2:
        # res = res + 1 if money % coins_sort[-1] == 0 else res
        for i in range(1, max_number[-1]+1):
            res += count_change(money - i * coins_sort[-1], coins_sort[:-1])
    coins_sort.pop()
    coins_trunc_tail = coins_sort
    return res + count_change(money, coins_trunc_tail)


print(count_change(14, [5, 7]))
print(count_change(4, [1, 2]))
print(count_change(10, [5,2,3,2]))
# print(count_change(10, [5 ,2,3]))


'better solution , and beautiful '

def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])