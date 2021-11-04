class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print("close-open")
    
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        if nums[mid] == target:
            return mid
        return -1
    
    # ================================================
    
    #Binary Search [O(logn), 39%]
    def search1(self, nums: List[int], target: int) -> int:
        print("Jiuzhang: open-open")
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