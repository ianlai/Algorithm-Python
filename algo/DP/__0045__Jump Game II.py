class Solution:
    
    #2022/02/14
    #DP[O(n2): 5%]
    def jump(self, nums: List[int]) -> int:
        dp = [inf] * len(nums)
        dp[0] = 0
        for i, v in enumerate(nums):
            for j in range(1, v+1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[-1]