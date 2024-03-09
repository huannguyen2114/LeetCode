class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, sum = 0, 0, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                sum = max(sum, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return sum