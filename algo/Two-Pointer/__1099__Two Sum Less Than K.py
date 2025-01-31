class Solution:
    
    # Two-Pointer [O(n), 94%]
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1
        
        maxSum = -float('inf')
        while left < right:
            twoSum = nums[left] + nums[right]
            if twoSum >= k:
                right -= 1
            else:
                left += 1
                maxSum = max(twoSum, maxSum)
        return maxSum if maxSum != -float('inf') else -1
                
            