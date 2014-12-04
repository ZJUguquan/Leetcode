
'Best Time to Buy and Sell Stock II '



1,2,3,10

"""
1 buy 2 sell  3 buy  10 sell : profit : sum(sell) - sum(buy)

1 buy 10 sell        profit:
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
        	return 0
        if len(prices) == 2:
        	return [prices[1] - prices[0] > 0 and prices[1] - prices[0] or 0][0]
        total = 0
        for i in range(1, len(prices)):
        	if prices[i] > prices[i-1]:
        		total += prices[i] - prices[i-1]
        return total

s = Solution()
print s.maxProfit([2,1]) #,5,7,1,10])