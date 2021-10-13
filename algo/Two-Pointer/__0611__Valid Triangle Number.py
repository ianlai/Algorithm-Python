class Solution:
    
    # Two-Sum [O(n2): 50%]
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for idx in range(len(nums)-1, -1, -1):
            res += self.twoSumLarger(nums, nums[idx], 0, idx - 1)
        return res
    
    def twoSumLarger(self, nums, target, l, r):
        count = 0 
        while l < r:
            twoSum = nums[l] + nums[r]
            if twoSum > target:  #valid number
                count += r - l 
                r -= 1
            else:
                l += 1
        return count 