class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices) -1
        sell = 0
        buy = 0
        res = 0
        while i < n:
            while i < n and prices[i+1] <= prices[i]:
                i+=1
            buy = prices[i]
                # res = max(res, sell - buy)
                #print(buy)
            while i< n and  prices[i+1] > prices[i] :
                i+=1
                
            sell = prices[i]
                #print(sold)
            res = res + (sell - buy)
            
            i += 1
        
        return res
        
        
