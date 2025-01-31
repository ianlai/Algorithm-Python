class Solution:
    
    # Sorting + Two pointer [O(nlogn): 16% / O(1): 64%]
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left, right = 0, len(nums)-1
        count = 0
        while left < right:
            sumup = nums[left] + nums[right]
            if sumup > k:
                right -= 1
            elif sumup < k:
                left += 1
            else:
                count += 1
                right -= 1
                left += 1
        return count 