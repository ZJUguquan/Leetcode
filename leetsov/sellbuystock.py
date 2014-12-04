#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = "Stevey"
__project__ = ""

'Best Time to buy and sell stock'

'It done'
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        begin = prices[0]
        profit = 0
        for i in range(1,len(prices)):
        	begin = min(begin, prices[i])
        	profit = max(profit, prices[i] - begin)
        return profit
'Discuss'

      # if(prices==null||prices.length<=1){
      #       return 0;
      #   }
      #   int min=prices[0];
      #   int profit=0;
      #   for(int i=1;i<prices.length;i++){
      #       min = Math.min(min,prices[i]);
      #       profit = Math.max(profit, prices[i]-min);
      #   }
      #   return profit;

'First Submit  Time Limit Exceeded'

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        results = []
        # if prices == []:
        #     return None
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return (prices[1] - prices[0] > 0 and [prices[1] - prices[0]] or [0] )[0]
        for i in range(1, len(prices) - 1):
            buylist = prices[:i]
            selllist = prices[i:]
            pos_profit = max(selllist) - min(buylist)
            results.append(pos_profit)
        max_profit = max(results)
        return (max_profit>0 and [max_profit] or [0])[0]



# print min([1,2][1:1])

def maxProfit(prices):
    results = []
    # if prices == []:
    #     return None
    if len(prices) <= 1:
        return 0
    for i in range(1, len(prices) - 1):
        buylist = prices[:i]
        selllist = prices[i:]
        pos_profit = max(selllist) - min(buylist)
        results.append(pos_profit)
    max_profit = max(results)
    return (max_profit>0 and [max_profit] or [0])[0]
     # max_profit if max_profit > 0
    # return 0

prices = [1,2,3,4,5,6,1,2,3]
print maxProfit(prices)


print (3 > 2 and [3] or [2])