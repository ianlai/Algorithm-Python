class Solution:
    
    # 2022/01/21
    # Sliding window [O(n): 26%]
    # All input are positive numbers (easier)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return -1
        
        i = 0
        curSum = 0
        res = inf
        for j, v in enumerate(nums):
            curSum += v
            while curSum >= target:
                res = min(res, j - i + 1)
                curSum -= nums[i]
                i += 1
        return res if res != inf else 0