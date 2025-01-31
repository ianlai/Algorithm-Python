class Solution:
    
    # 2021/11/10
    # Binary Search [O(logn): 56%]
    def findPeakElement(self, nums: List[int]) -> int:
        print("close-open")
        if not nums:
            return -1
        
        start, end = 0, len(nums) 
        while start < end:
            mid = start + (end - start) //2
            #print(mid)
            if mid == len(nums) - 1:  #except (no next element)
                if nums[mid-1] < nums[mid]:
                    return mid
                else:
                    end = mid
            else:
                if nums[mid] < nums[mid+1]:
                    start = mid + 1
                else:
                    end = mid
        return start
    
    # ======================================
    
    # 2021/05/10
    # Binary Search [O(logn): 56%]
    def findPeakElement1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        print(start, end)
        if nums[start] > nums[end]:
            return start
        return end 