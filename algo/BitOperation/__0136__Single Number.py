class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        ans = 0
        for e in nums:
            ans ^= e
        return ans