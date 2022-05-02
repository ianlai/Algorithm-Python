class Solution:
    
    # 2022/05/02
    # In-place Partition [TC: O(n): 81% / Space: O(1): 17%]
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        print("Code3: Partition")
        left, right = 0, len(nums) - 1
        while left < right: 
            while left < right and nums[left] % 2 == 0:  #find odd
                left += 1
            while left < right and nums[right] % 2 == 1: #find even 
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums  
        
    # Partition [Time: O(n) 80% / Space: O(1) 93% ]
    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        print("Partition")
        if not nums:
            return []
        left, right = 0, len(nums) - 1 
        while left < right: 
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
    
    # ==================================================
    
    # Two List [Time: O(n) 58% / Space: O(n) 55% ]
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        print("Two List")
        if not nums:
            return []
        
        oddList = []
        evenList = []
        
        for num in nums:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
                
        evenList.extend(oddList)
        return evenList