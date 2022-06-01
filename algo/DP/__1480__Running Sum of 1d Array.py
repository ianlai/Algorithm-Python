class Solution:
    # 2022/06/01
    # DP [O(N): 58% / O(1): 94%]
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(dp[-1] + nums[i])
        return dp