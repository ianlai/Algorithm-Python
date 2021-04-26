class Solution:
    
    # Sorting (86%)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        nums = sorted(nums)[::-1]
        return nums[k-1]