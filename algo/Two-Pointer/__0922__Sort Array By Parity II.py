class Solution:
    
    # Partition + Traverse once to interleave [Time: O(n), 42% / Space: O(1), 95%]
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        print("Partition")
        if not nums:
            return []
        
        # Partition
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 0:
                left += 1 
            while left <= right and nums[right] % 2 == 1:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        #print(nums)
        
        # Interleave 
        for i in range(len(nums)//2):
            j = len(nums) - 1 - i
            if i % 2 == 1: 
                nums[i], nums[j] = nums[j], nums[i]
        return nums
                
    # ======================================================
    
    # Two extra lists [Time: O(n), 56% / Space: O(n), 89%]
    def sortArrayByParityII1(self, nums: List[int]) -> List[int]:
        print("Two extra lists")
        
        if not nums:
            return []
        evenList, oddList = [], []
        for num in nums:
            if num % 2 == 0:
                oddList.append(num)
            else:
                evenList.append(num)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = oddList.pop()
            else:
                nums[i] = evenList.pop()
        
        return nums