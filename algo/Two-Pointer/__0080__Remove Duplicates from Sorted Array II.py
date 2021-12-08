class Solution:
    
    # Two-Pointer [O(n): 85%]
    def removeDuplicates(self, nums: List[int]) -> int:
    
        if len(nums) < 3:
            return len(nums)
        
        cur = 0 
        for i in range(len(nums)):
            if i < len(nums) - 3: 
                if not (nums[i] == nums[i+1] == nums[i+2]):
                    nums[cur] = nums[i]
                    cur += 1
            elif i == len(nums) - 3:
                if not (nums[i] == nums[i+1] == nums[i+2]):
                    nums[cur] = nums[i]
                    nums[cur+1] = nums[i+1]
                    nums[cur+2] = nums[i+2]
                    cur += 3
                else:
                    nums[cur] = nums[i]
                    nums[cur+1] = nums[i+1]
                    cur += 2
        return cur