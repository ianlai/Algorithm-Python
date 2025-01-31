class Solution:
    
    #Greedy [O(n): 79%]
    def canJump(self, nums: List[int]) -> bool:
        nums = nums[::-1]
        target = 0
        for i, v in enumerate(nums):
            if i == 0:
                continue
            if v >= i - target:
                target = i
        return target == len(nums) - 1