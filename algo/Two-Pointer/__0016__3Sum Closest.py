class Solution:
    
    # Sorting, For loop: A, Two-Pointers: B+C  [O(nlogn), 83%]
    # since we only need an answer, we don't need to remove the duplication
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        
        print(nums)
        
        closedSum  = 0 
        minDiff = float('inf')
        
        for first in range(len(nums)):
            left, right = first + 1, len(nums) - 1
            
            while left < right: 
                threeSum = nums[first] + nums[left] + nums[right]
                if threeSum == target:
                    return target
                elif threeSum > target:
                    if abs(threeSum - target) < minDiff:
                        closedSum = threeSum 
                        minDiff = abs(threeSum - target)
                    right -= 1
                else:
                    if abs(threeSum - target) < minDiff:
                        closedSum = threeSum 
                        minDiff = abs(threeSum - target)
                    left += 1
        return closedSum