class Solution:
    
    # Bidirectional kadane algorithm [O(n): 39%]
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = inf
        maxProfit = 0
        leftProfit = [0] * len(prices)
        for i, p in enumerate(prices):
            minPrice = min(minPrice, p)
            maxProfit = max(maxProfit, p - minPrice)
            leftProfit[i] = maxProfit
        
        maxPrice = -inf
        maxProfit = 0
        rightProfit = [0] * len(prices)
        for i in range(len(prices)-1, -1, -1):
            p = prices[i]
            maxPrice = max(maxPrice, p)
            maxProfit = max(maxProfit, maxPrice - p)
            rightProfit[i] = maxProfit
            
        #print(leftProfit)
        #print(rightProfit)
            
        maxProfitTwo = leftProfit[-1]
        for i in range(1, len(leftProfit)):
            maxProfitTwo = max(maxProfitTwo, leftProfit[i-1] + rightProfit[i])
        return maxProfitTwo