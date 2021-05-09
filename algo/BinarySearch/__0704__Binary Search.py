class Solution:
    
    #Binary Search [O(logn), 39%]
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1
            