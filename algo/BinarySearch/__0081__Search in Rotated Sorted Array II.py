# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    
    # 2022/03/28 
    # Implement Binary Search Left and use the function twice [O(logn): 77%]
    def search(self, nums: List[int], target: int) -> bool:
        print("Code2")
        def binarySearch(start, end, target):
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] > nums[-1]:
                    start = mid + 1
                else:
                    end = mid
            return start  #leftmost 
                    
        start = 0
        for i, v in enumerate(nums):
            if v == target:
                return True
            if nums[i] != nums[-1]:
                start = i
        
        end = len(nums)
        minIdx = binarySearch(start, end, nums[-1])
        idx = 0
        if target <= nums[-1]:
            idx = binarySearch(minIdx, end, target)
        else:
            idx = binarySearch(start, minIdx-1, target)
        return True if nums[idx] == target else False

    # =========================================================
    
    # 2021/12/14
    # Binary Search [Avg case: O(log), worst case: O(n) -> 76%]
    def search1(self, nums: List[int], target: int) -> bool:
        print("Code1")
        
        # (1) Exception 
        if target == nums[-1]:
            return True
        
        # (2) Find last item smaller than nums[-1]
        lastIdx = len(nums) - 1
        while lastIdx > 0:
            if nums[lastIdx] != nums[-1]:
                break
            lastIdx -= 1
        if target == nums[lastIdx]:
            return True
        if lastIdx == 0:
            return False
        
        # (3) Search min
        start, end = 0, lastIdx
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[lastIdx]:    #right
                end = mid 
            else:
                start = mid + 1
        minIdx = start 
        
        # (4) Determine the search interval should be left or right
        if target < nums[lastIdx]:
            start, end = minIdx, lastIdx 
        else:
            start, end = 0, minIdx
        
        # (5) Search for the target 
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1 
            else:
                end = mid
        return False