MAX_VAL = float('inf')

class Solution:

    # Buttom-Up DP [Time: 23% / Space:22%]
    def coinChange(self, coins: List[int], amount: int) -> int:
        print("Bottom-Up DP")
        
        # Initialize
        dp = [[inf for _ in range(amount+1)] for _ in range(len(coins))]
        for row in dp:
            row[0] = 0
            
        # DP loop
        for i, coin in enumerate(coins):
            for j in range(amount+1):
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                    continue
                if i == 0 and j - coin >= 0:
                    dp[i][j] = dp[i][j-coin] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coin] + 1) 

        return dp[-1][-1] if dp[-1][-1] != inf else -1
    
    # =====================================================
    
    # Top-Down DP [Time: 5% / Space: 5%]
    def coinChange1(self, coins: List[int], amount: int) -> int:
        print("Top-Down DP")
        def dfs(coins, amount, idx, cur, minNum, memo):
            if amount < 0:
                return MAX_VAL
            if amount == 0:
                #return min(len(cur), minNum) #WRONG
                return 0
            if amount in memo:
                return memo[amount]
            
            localMin = MAX_VAL
            #for i in range(0, len(coins)):  #WRONG
            for i in range(0, len(coins)):
                localMin = min(localMin, 1 + dfs(coins, amount - coins[i], i, cur + [coins[i]], minNum, memo))
            memo[amount] = localMin
            return memo[amount] 
            
        if len(coins) == 0 and amount == 0:
            return 0
        if len(coins) == 0 and amount != 0:
            return -1
        memo = {}
        amountList = [MAX_VAL] * (amount + 1)
        minNum = dfs(coins, amount, 0, [], MAX_VAL, memo)
        return minNum if minNum != MAX_VAL else -1
    
    #=====================================================

    # DP (memoization), with return value [10%] 
    def coinChange1(self, coins: List[int], amount: int) -> int:
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