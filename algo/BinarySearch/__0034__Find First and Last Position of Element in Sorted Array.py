class Solution:
    
    # 2021/12/11 
    # Binary Search [O(logn): 29%]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print("Code-2")
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target: #left part: <=, right part: >, find last left 
                start = mid + 1
            elif nums[mid] > target: 
                end = mid
        ans1 = start - 1 if start != 0 and nums[start - 1] == target else -1 

        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < target: #left part: <, right part: >=, find first right 
                start = mid + 1
            elif nums[mid] >= target: 
                end = mid
        ans2 = start if start != len(nums) and nums[start] == target else -1
        
        return [ans2, ans1]
        
    # ====================================================
    # 2021/11/09
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        print("Code-1")
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