class Solution:
    
    # 2021/12/13
    # Jump out if found
    def search5(self, nums: List[int], target: int) -> int:
        print("Code5")
        start, end = 0, len(nums)
        while start < end :
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid +1 
        return -1 
    
    # ================================================
    # 2021/12/13
    # Until the searching interval is empty 
    def search(self, nums: List[int], target: int) -> int:
        print("Code4")
        start, end = 0, len(nums)
        while start < end :
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            else:
                start = mid +1 
        return start if start != len(nums) and nums[start] == target else -1 

    # ================================================

    # 2021/11/08
    # Originally, "<="" MUST find the answer inside the loop to return 
    # To fix it, we can remove "=" condition in loop, and force it to move the s, e always,
    # However, then we need to let [s, e] to be the possible index 
    def search3(self, nums: List[int], target: int) -> int:
        print("Code3: close-open, less than equal to")
    
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
    
    # 2021/11/04 (ok)
    # BEST
    # When start == end, it will jump out from loop, and start point at correct partition 
    # Example: 
    # [0,2,4,6] -> s=0, e=4 (not 3)
    # target:
    # -1 ->   start = 0  (not found) 
    # 0  => mid   = 0  (found)
    # 1  ->   start = 1  (not found) 
    # 2  => mid   = 1  (found)
    # 3  ->   start = 2  (not found) 
    # 4  => mid   = 2  (found)
    # 5  ->   start = 3  (not found) 
    # 6  => mid   = 3  (found)
    # 7  ->   start = 4  (not found) 
    # So mid can search all element; if not found, start can search all intervals
    def search2(self, nums: List[int], target: int) -> int:
        print("Code2: close-open, less than (BEST)")
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            print("s:", start, "e:", end, "mid:", mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1
        print("start:", start)
        return -1
    
    # ================================================
    
    # 2021/05/09
    #Binary Search [O(logn), 39%]
    def search1(self, nums: List[int], target: int) -> int:
        print("Code1: Jiuzhang, open-open")
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