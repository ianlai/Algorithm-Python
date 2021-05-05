class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        revenue = 0
        minVal = prices[0]
        
        for i in range(1, len(prices)):
            minVal = min(minVal, prices[i-1])
            #go up and down (sell at the peak)
            if i >= 2 and prices[i-1] >= prices[i] and prices[i-2] <= prices[i-1]:
                revenue += prices[i-1] - minVal
                minVal = prices[i]
                
        #last chance (sell in the end)
        if prices[-1] > minVal:
            revenue += prices[-1] - minVal
            
        return revenue 