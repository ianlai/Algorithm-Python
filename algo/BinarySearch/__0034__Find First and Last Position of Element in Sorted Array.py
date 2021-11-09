class Solution:

    # 2021/11/09
    # Binary Search [O(logn), 92%] 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1] 
        
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid 
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid 
                
        if start < len(nums) and nums[start] == target:
            first = start
        else:
            first = -1
        
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid + 1 
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid 
                
        start -= 1
        if start < len(nums) and nums[start] == target:       
            last = start
        else:
            last = -1
        
        return [first, last]

    # ==================================================
    
    # 2021/05/09
    # Binary Search [O(logn), 68%]  
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        firstIdx, lastIdx = -1, -1 
        
        # Find first position 
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:  #not done yet, continue
                end = mid 
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid 
                
        print("firstIdx:", start, end)
        if nums[start] == target:  #start (left) should check first
            firstIdx = start
        elif nums[end] == target:
            firstIdx = end 
    
        # Find last position
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:  #not done yet, continue
                start = mid 
            if nums[mid] < target:
                start = mid
            if nums[mid] > target:
                end = mid 
                
        print("lastIdx:", start, end)
        if nums[end] == target:  #end (right) should check first
            lastIdx = end
        elif nums[start] == target:
            lastIdx = start 
            
        return [firstIdx, lastIdx]