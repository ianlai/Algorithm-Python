class Solution:      
    
    # 2022/02/16
    # DP 1D [O(n): 38%]
    def rob(self, nums: List[int]) -> int:
        print("Code2")
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
        
    # ==============================    
    # DP 2D [O(n): 5%]
    def rob1(self, nums: List[int]) -> int:
        print("Code1")
        dp = [[0 for _ in range(2)] for _ in range(len(nums))] #use, not use
        dp[0][0] = nums[0]
        dp[0][1] = 0
        for i, v in enumerate(nums):
            if i == 0:
                continue
            dp[i][0] = dp[i-1][1] + nums[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
        return max(dp[-1][0], dp[-1][1])