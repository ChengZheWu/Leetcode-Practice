# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
1. DP

T: O(n)
S: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for sell in prices:
            min_buy = min(min_buy, sell)
            max_profit = max(max_profit, sell - min_buy)
        return max_profit

'''
2. Two Pointers

T: O(n)
S: O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[r] >= prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit