class Solution:
    
    # Bottom-Up DP (array) [time: 74%]  
    def combinationSum4(self, nums: List[int], target: int) -> int:    
        print("Bottom-Up DP (array)")
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num < 0:
                    continue
                dp[i] += dp[i - num]
        return dp[-1]    
    
    #===============================================================

    # Bottom-Up DP (matrix) [time: 5%]  
    def combinationSum41(self, nums: List[int], target: int) -> int:    
        print("Bottom-Up DP (matrix)")
        dp = [[0 for _ in range(target + 1)] for _ in range(target + 1)]
        for row in dp:
            row[0] = 1
            
        for i in range(target + 1):
            if i == 0: 
                for num in nums:
                    if i + num > target:
                        continue
                    dp[i][i + num] = dp[i][i]
            else:
                for j in range(target + 1):
                    dp[i][j] = dp[i-1][j]
                for num in nums:
                    if i + num > target:
                        continue
                    dp[i][i + num] = dp[i][i] + dp[i-1][i + num]
        return dp[-1][-1]
        
    #===============================================================
    # Top-Down DP [38%]
    def combinationSum41(self, nums: List[int], target: int) -> int:   
        print("Top-Down DP")
        res = []
        memo = {}
        count = self.dfs(nums, target, memo)
        return count
    
    def dfs(self, nums, target, memo):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in memo:
            return memo[target]
        
        count = 0
        for i in range(len(nums)):
            count += self.dfs(nums, target - nums[i], memo)
        memo[target] = count
        return count 
            
    #===============================================================
    
    #DFS [TLE]
    def combinationSum41(self, nums: List[int], target: int) -> int:    
        res = []
        self.dfs1(nums, target, [], res)
        return len(res)
    
    def dfs1(self, nums, target, cur, res):
        if target < 0:
            return 
        if target == 0:
            res.append(cur)
            return 
        
        for i in range(len(nums)):
            self.dfs1(nums, target - nums[i], cur + [nums[i]], res)
        