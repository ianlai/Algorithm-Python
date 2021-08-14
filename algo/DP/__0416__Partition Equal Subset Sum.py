class Solution:
    
    # Tabulation DP [O(n * sum/2)]
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2

        reachable_sum = {0}
        for num in nums:
            if target - num in reachable_sum:
                return True
            next_sum = {n + num for n in reachable_sum if n + num < target}
            reachable_sum.update(next_sum)
        return False
    
    # ==============================================
    
    # Tabulation DP [O(n * sum/2) : 36%]
    def canPartition(self, nums: List[int]) -> bool:
        print("TTT")
        # find sum of array elements
        total_sum = sum(nums)

        # if total_sum is odd, it cannot be partitioned into equal sum subsets
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2

        # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]
    # ==============================================
    # Tabulation DP [O(n * sum/2) : 36%]
    def canPartition2(self, nums: List[int]) -> bool:
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