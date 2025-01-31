class Solution:
    
    # 2022/06/11
    # Sliding window [O(N): 81% / O(1): 62%]
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0 :
            return len(nums)
        
        mylen, mysum = 0, 0
        left = 0
        for right in range(len(nums)):
            mysum += nums[right]
            
            while left < right and mysum > target:
                mysum -= nums[left]
                left += 1
                
            if mysum == target:
                mylen = max(mylen, right - left + 1)
            
        return len(nums) - mylen if mylen != 0 else -1