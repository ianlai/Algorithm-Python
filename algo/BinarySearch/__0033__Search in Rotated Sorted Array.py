class Solution:
    
    # Binary Search Twice (min -> target) [O(logn), 69%]
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        
        start, end = 0, len(nums) - 1
        minVal = nums[-1]
        minIdx = 0
        while start + 1 < end: 
            mid = start + (end - start) // 2
            if nums[mid] <= minVal:
                end = mid
            else:
                start = mid 
        if nums[start] < nums[end]:
            minIdx = start
            minVal = nums[start]
        else:
            minIdx = end
            minVal = nums[end]
            
        #print(minIdx, minVal)
            
        if minVal <= target <= nums[-1]:
            start, end = minIdx, len(nums) - 1
        else:
            start, end = 0, minIdx - 1 
            
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1