class Solution:
    
    # Originally, "<="" MUST find the answer inside the loop to return 
    # To fix it, we can remove "=" condition in loop, and force it to move the s, e always,
    # However, then we need to let [s, e] to be the possible index 
    def search(self, nums: List[int], target: int) -> int:
        print("close-open, less than equal to")
    
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        #ok
        if target == nums[start-1]:
            return start-1
        #ok
        # if target == nums[end]:
        #     return end
        return -1
    
    # ================================================
    
    # When start == end, it will jump out from loop, and start point at correct partition 
    def search1(self, nums: List[int], target: int) -> int:
        print("close-open, less than")
    
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
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