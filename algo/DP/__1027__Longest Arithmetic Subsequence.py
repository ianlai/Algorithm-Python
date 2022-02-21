class Solution:
    
    # 2022/02/21
    # DP (use 2D defaultdict) [O(n2): 20%]
    def longestArithSeqLength(self, nums: List[int]) -> int:
        print("Code2")
        dp = collections.defaultdict(lambda :collections.defaultdict(lambda:1))
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] = dp[j][nums[i] - nums[j]] + 1
                res = max(res, dp[i][nums[i] - nums[j]])
        return res
    
    
    # DP (use tuple as key) [TLE]
    def longestArithSeqLength1(self, nums: List[int]) -> int:
        print("Code1")
        dp = collections.defaultdict(lambda:1)
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                dp[(i, nums[i] - nums[j])] = dp[(j, nums[i] - nums[j])] + 1
                res = max(res, dp[(i, nums[i] - nums[j])])
        return res