class Solution:
    
    # DP (memoization), with return value [10%] 
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0:
            return -1
        
        memo = {}
        ans = self.dfs(coins, amount, memo) #removed ans[], cur[], index
        
        return -1 if ans == float('inf') else ans
        
    def dfs(self, coins, amount, memo):
        #memoization
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0 
        if amount in memo:
            return memo[amount] 
        
        result = float('inf')
        for i in range(len(coins)):
            #result = min(result, 1 + self.dfs(coins, amount - coins[i], i, memo))   # "i" means not repeated
            #result = min(result, 1 + self.dfs(coins, amount - coins[i], idx, memo)) # "idx" means repeated is allowed (then idx is not needed)
            result = min(result, 1 + self.dfs(coins, amount - coins[i], memo))      # removed index

        memo[amount] = result
        return result
        
    
      # DP (memoization), with answer array 
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         if coins is None or len(coins) == 0:
#             return -1
        
#         ans = [float('inf'), float('inf')]
#         memo = {}
#         self.dfs(coins, amount, 0, [], ans, memo)
        
#         #print(memo)
#         #print(ans)
        
#         return -1 if ans[0] == float('inf') else ans[0]
        
        
#     def dfs(self, coins, amount, idx, cur, ans, memo):
#         #memoization
#         if amount < 0:
#             ans[1] = memo[amount] = -1
#             return 
        
#         if amount in memo:
#             ans[1] = memo[amount]
#             return 

#         if amount == 0:
#             ans[0] = min(ans[0], len(cur))
#             return
        
#         for i in range(idx, len(coins)):
#             self.dfs(coins, amount - coins[i], i, cur + [coins[i]], ans, memo)
#         memo[amount] = ans[1]
        
    #=======================================================================
    
    #DFS: TLE 
    def coinChange1(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0:
            return -1
        
        ans = [float('inf')]
        self.dfs1(coins, amount, 0, [], ans)
        
        return -1 if ans[0] == float('inf') else ans[0]
        
        
    def dfs1(self, coins, amount, idx, cur, ans):
        if amount < 0:
            return 
        if amount == 0:
            ans[0] = min(ans[0], len(cur))
            return 
        for i in range(idx, len(coins)):
            self.dfs1(coins, amount - coins[i], i, cur + [coins[i]], ans)
        