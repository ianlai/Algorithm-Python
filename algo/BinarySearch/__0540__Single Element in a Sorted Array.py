class Solution:
    
    # 2021/12/12
    # Binary Search (loop invariant considered) [O(logn): 6%]
    def singleNonDuplicate(self, nums):
        print("Code4")
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if mid == 0:
                return nums[mid]
            if mid == len(nums) - 1:
                return nums[mid]
                
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    start = mid + 2
                elif nums[mid-1] == nums[mid]:
                    end = mid - 1 
            else:
                if nums[mid-1] == nums[mid]:
                    start = mid + 1
                elif nums[mid] == nums[mid+1]:
                    end = mid 
        return start 
                
    # ==================================
    # 2021/08/06
    # Binary Search [7%]
    def singleNonDuplicate3(self, nums):
        print("Code3")
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid
        #print(left, right)
        if left % 2 == 0:
            return nums[left]
        return nums[right]

    # ==================================
    # Binary Search [O(logn): 10%]
    def singleNonDuplicate2(self, nums: List[int]) -> int:
        print("Code2")
        #Special case
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]
        
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]: 
                return nums[mid]
            
            if nums[mid] == nums[mid + 1]:
                mid = mid 
            elif nums[mid-1] == nums[mid]:
                mid = mid - 1

            leftCount = (mid - 1) - start + 1
            if leftCount % 2 == 0:
                start = mid + 2 
            else:
                end = mid - 1 
        
        if nums[start-1] < nums[start] < nums[start+1]:
                return nums[start]
        if nums[end-1] != nums[end] and nums[end] != nums[end+1]: 
                return nums[end]
        return -1
    
    # ==================================
    # XOR [O(n): 6%]
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        print("Code1")
        x = 0
        for i in nums:
            x ^= i
        return x