class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Define 3 variables: i (index), buy (price at the time to buy), sell (price at the time to sell), res (result)
        i, buy, sell, res = 0, 0, 0, 0
        # [7, 1, 5, 3, 6, 4]
        #              |  |
        # i          buy sell
        while i < len(prices):
            # The time to buy is the smallest number in strictly decreasing sequence
            while i < len(prices) - 1 and prices[i + 1] < prices[i]:
                i += 1
            buy = prices[i]

            # The time to sell is the highest number in increasing sequence
            while i < len(prices) - 1 and prices[i+1] >= prices[i]:
                i += 1
            sell = prices[i]

            # Compute res at the time
            res += (sell - buy)

            i += 1
        return res
            