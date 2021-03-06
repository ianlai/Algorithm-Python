class Solution:
    
    # Buttom-Up DP, 1D array [Time O(m*n): 24% / Space O(n): 47%]
    # 利用dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]] 右邊前半部直接在j點相等的這個點
    # 可以直接把式子中的i退化掉，變成dp[j] = dp[j] + dp[j-coins[i]]
    # 所以DP的過程雖然是雙層回圈，但dp卻可以改成完全的一維陣列
    #（甚至連平常space optimization需要2*n的2都可以省掉了）
    def change(self, amount: int, coins: List[int]) -> int:
        print("Buttom-Up DP with space optimization, 1D array")
        
        dp = [0 for _ in range(amount+1)]
        
        # Initialize
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
                    
        return dp[-1]
    
    # =====================================================

    # Buttom-Up DP, 2d matrix [Time O(m*n): 24% / Space O(n): 47%]
    def change1(self, amount: int, coins: List[int]) -> int:
        print("Buttom-Up DP with space optimization")
        
        dp = [[0 for _ in range(amount+1)] for _ in range(2)]
        
        # Initialize
        for i in range(2):
            dp[i][0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                dp[i%2][j] = dp[(i-1)%2][j]           #Num of methods of not-using coins[i]
                if j >= coins[i]:
                    dp[i%2][j] += dp[i%2][j-coins[i]] #Num of methods of using coins[i]
                    
        return max(dp[0][-1], dp[1][-1])
    
    # =====================================================

    # Buttom-Up DP [Time O(m*n): 24% / Space O(m*n): 19%]
    def change1(self, amount: int, coins: List[int]) -> int:
        print("Buttom-Up DP")
        
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        
        # Initialize
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]             #Num of methods of not-using coins[i]
                if j >= coins[i]:
                    dp[i][j] += dp[i][j-coins[i]] #Num of methods of using coins[i]
        #print(dp)
        return dp[-1][-1]
    
    # =====================================================
    
    # Top-Down DP [TLE]
    def change1(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        if not coins:
            return 0
        print("Top-Down DP")
        
        self.count = 0
        self.coins = [] 
        
        #prune 
        for coin in coins:
            if coin <= amount:
                self.coins.append(coin)
        
        res = []
        memo = collections.defaultdict(int)
        return self.dfs(amount, [], 0, res, memo)
    
    def dfs(self, amount, cur, idx, res, memo):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if (idx, amount) in memo:   #Memoization DP 
            return memo[(idx, amount)]
        
        count = 0
        for i in range(idx, len(self.coins)):
            count += self.dfs(amount - self.coins[i], cur + [self.coins[i]], i, res, memo)
        memo[(idx, amount)] = count
        return count 