class Solution:
    
    # 2022/01/13
    # Single pass, sum up all diff between i and i-1  (Approach3) [O(n): 58%]
    def maxProfit(self, prices: List[int]) -> int:
        print("Code3")
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] -  prices[i-1] 
            profit += prices[i] - prices[i-1] if diff > 0 else 0
        return profit
        
    # ========================================
    # 2022/01/13
    # Single pass, sum up the diff between valley and peak (Approach2) [O(n): 24%]
    def maxProfit2(self, prices: List[int]) -> int:
        print("Code2")
        profit = 0 
        for i, v in enumerate(prices):
            if i == 0:
                buy = (i, v)
            if i > 0 and prices[i-1] > prices[i]:
                if i - 1 > buy[0] and prices[i-1] > buy[1]:
                    profit += prices[i-1] - buy[1]
                buy = (i, v)
        profit += prices[-1] - buy[1]
        return profit

    # ========================================
    # 2021/05/05
    # Single pass [O(n):23%]
    def maxProfit1(self, prices: List[int]) -> int:
        print("Code1")
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