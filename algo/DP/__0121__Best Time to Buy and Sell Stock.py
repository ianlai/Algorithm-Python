class Solution:
    
    # Find min from each point, compare prev and lastMin [O(n), 21%]
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
    
        lastMin = prices[0]
        revenue = 0
        for i in range(1, len(prices)):
            thisMin = min(lastMin, prices[i-1])
            lastMin = thisMin
            revenue = max(prices[i] - thisMin , revenue)
        return revenue
    
    
    # Find min from each point to the left [O(n2), TLE]
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        revenue = 0
        for i in range(1, len(prices)):
            revenue = max(prices[i] - min(prices[:i]), revenue)
        return revenue