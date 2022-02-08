class Solution:

    # 2022/02/08 
    # Binary search [O(logn): 30%]
    def searchInsert(self, nums: List[int], target: int) -> int:
        print("Code2")
        
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            else:
                start = mid + 1 
        return start
    
    
    # 2022/02/08 
    # Bisect [O(logn): ]
    def searchInsert1(self, nums: List[int], target: int) -> int:
        print("Code1")
        return bisect.bisect_left(nums, target)