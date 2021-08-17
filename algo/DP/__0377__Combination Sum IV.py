class Solution:
    
    # Top-Down DP [38% ]
    def combinationSum4(self, nums: List[int], target: int) -> int:    
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
        