class Solution:
    
    # Greedy [O(n): 33%]
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        for i, v in enumerate(nums):
            if count % 2 == 0:
                if i % 2 == 1 and nums[i-1] == nums[i]:
                    count += 1
            else:
                if i % 2 == 0 and nums[i-1] == nums[i]:
                    count += 1
        if (len(nums) - count) % 2 != 0:
            count += 1
        return count 
                
                
        