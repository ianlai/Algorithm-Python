class Solution:
    
    # Partition twice [O(n), 8%]
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print("Partition twice")
        if not nums:
            return 
        
        left, right = 0, len(nums) - 1 
        while left <= right:
            while left <= right and (nums[left] == 0 or nums[left] == 1):
                left += 1
            while left <= right and nums[right] == 2:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        left, right = 0, left - 1
        while left <= right:
            while left <= right and nums[left] == 0:
                left += 1
            while left <= right and nums[right] == 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return 
            
    # =============================================
    # Counting Sort [O(n), 8%]
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print("Counting Sort")
        if not nums:
            return 
        
        counts = [0] * 3
        
        #count 
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        #fill in the values
        idx = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[idx] = i
                idx += 1
        return 
    
    # =============================================
    # Built-in Sorting [O(nlogn), 8%]
    def sortColors0(self, nums: List[int]) -> None:
        print("Built-in Sorting")
        nums.sort()