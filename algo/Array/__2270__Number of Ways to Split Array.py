class Solution:
    
    # One pass [O(N) : 100 % / O(1): 80 %]
    def waysToSplitArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 0
        left, right = 0, sum(nums)
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right: 
                count += 1
        return count