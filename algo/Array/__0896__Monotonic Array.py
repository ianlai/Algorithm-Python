class Solution:
    
    # 2022/03/30 
    # Scan array [O(n): 95%]
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = None
        isDecreasing = None
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i-1] < nums[i]:
                isIncreasing = True
            elif nums[i-1] > nums[i]:
                isDecreasing = True
            if isIncreasing and isDecreasing:
                return False
        return True
                