class Solution:
    
    # Partition [Time: O(n) 80% / Space: O(1) 93% ]
    # half even elements, then half odd elements
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        print("Partition")
        if not nums:
            return []
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