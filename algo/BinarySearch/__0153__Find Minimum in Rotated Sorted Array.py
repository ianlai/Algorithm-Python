class Solution:
    
    # Binary Search [O(logn), 96%]
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if nums[mid] > nums[0]:
                start = mid
            else:
                end = mid
                
        return min(nums[0], min(nums[start], nums[end])) #asc is special case