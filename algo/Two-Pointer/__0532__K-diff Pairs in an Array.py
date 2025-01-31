class Solution:
    
    # Two-pointer 同向雙指針, remove redundants with set [O(n), 35%]
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        left, right = 0, 0
        ans = set([])
        while left < len(nums) and right < len(nums):
            if left == right:
                right += 1 
                continue
            diff = nums[right] - nums[left]
            if diff < k :
                right += 1
            elif diff == k:
                ans.add((nums[right], nums[left]))
                left += 1 
                right += 1
            else:
                left += 1 
        #print(ans)
        return len(ans)