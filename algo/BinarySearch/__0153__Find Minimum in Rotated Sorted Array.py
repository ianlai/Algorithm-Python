class Solution:
    # 2021/11/06
    # Close-open interval
    def findMin(self, nums: List[int]) -> int:
        print("Version-3")
        if not nums: 
            return -1
        
        start, end = 0, len(nums)
        target = nums[-1]
        while start < end:
            mid = start + (end - start) // 2
            if target >= nums[mid]:
                end = mid
            else:
                start = mid + 1
        return nums[start]
    
    # =========================================
    # 2021/07/15
    # Close-close interval (Jiuzhang)
    def findMin2(self, nums: List[int]) -> int:
        print("Version-2")
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if nums[mid] <= target: 
                end = mid
            else:                   
                start = mid
                
        return min(nums[start], nums[end]) #no special case judgement
    
    # =========================================
    # 2021/05/10
    # Binary Search [O(logn), 96%]
    def findMin1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        
        target = nums[0]
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if nums[mid] > target: # >= first (left xxx) 
                start = mid
            else:                   # < first (right ooo) , but asc order can't be found
                end = mid
                
        return min(nums[0], min(nums[start], nums[end])) #asc is special case 