class Solution:

    
    # Close-Open Binary Search [O(logn): 81%]
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # Step1: Find min
        start, end = 0, len(nums)
        last = nums[-1]
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= last:
                end = mid
            else:
                start = mid + 1
        minVal, minIdx = nums[start], start
        print("minIdx:", minIdx, "minVal:", minVal)
        
        # Step2: Find target in left or right intervals
        if target <= last:  #right interval 
            start, end = minIdx, len(nums)
        else:
            start, end = 0, minIdx #[0, minIdx-1] 
        while start < end: 
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid 
        return -1 
    
    # ===================================================
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