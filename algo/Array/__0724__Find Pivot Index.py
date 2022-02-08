class Solution:
    
    # 2022/02/08 
    # Array [O(n): 45%]
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums) 
        leftTotal = 0 
        for i in range(len(nums)):
            if i > 0:
                leftTotal += nums[i-1]
            total -= nums[i]
            if leftTotal == total:
                return i
        return -1