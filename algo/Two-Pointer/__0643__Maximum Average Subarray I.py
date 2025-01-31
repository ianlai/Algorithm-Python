class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return None
        
        maxTotal = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i-k]
            maxTotal = max(maxTotal, total)
        return maxTotal / k 