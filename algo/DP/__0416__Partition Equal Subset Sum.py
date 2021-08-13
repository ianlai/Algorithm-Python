class Solution:
    
    # Tabulation DP [O(n * sum/2) : 36%]
    def canPartition(self, nums: List[int]) -> bool:
        print("Tabulation")
        if not nums:
            return True
        allSum = sum(nums) 
        if allSum % 2 != 0:
            return False
        target = int(allSum / 2)
        print("target=", target)
        
        # Initialize
        dp = [[0 for _ in range(target+1)] for _ in range(len(nums))]
        dp[0][0] = 9
        if nums[0] < len(dp):
            dp[0][nums[0]] = 9 
        
        # DP
        for i in range(1, len(nums)):
            for j in range(target):
                if dp[i-1][j]:
                    if j + nums[i] <= target:
                        dp[i][j+nums[i]] = 1
                    dp[i][j] = 1
                    
        # for i in range(len(dp)):
        #     print(dp[i])
        
        for i in range(len(nums)):
            if dp[i][target] == 1:
                return True
        return False
    
    # ==============================================
    # Memoization DP [O(sum/2) : 74%]
    def canPartition1(self, nums: List[int]) -> bool:
        print("Memoization")
        if not nums:
            return True
        allSum = sum(nums) 
        if allSum % 2 != 0:
            return False
        target = allSum / 2 
        memo = set()
        return self.targetSum(nums, 0, target, memo)
        
    def targetSum(self, nums, idx, target, memo):
        if target == 0:
            return True
        if target in memo:
            return False
        if idx >= len(nums):
            return False
        
        if self.targetSum(nums, idx + 1, target - nums[idx], memo):
            return True
        if self.targetSum(nums, idx + 1, target, memo):
            return True
        memo.add(target) 
        return False