from typing import List
import unittest
class Solution:
    
    # 2022/06/12
    # Prefix Sum + Sliding Window [O(N): 35% / O(N): 30%]
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])

        maxScore = 0
        left = 0
        charSet = set()
        for right in range(len(nums)):
            while nums[right] in charSet:
                charSet.remove(nums[left])
                left += 1
            charSet.add(nums[right])
            if left > 0: 
                maxScore = max(maxScore, prefixSum[right] - prefixSum[left - 1])
            else:
                maxScore = max(maxScore, prefixSum[right])
        return maxScore
sol = Solution()
print(sol.maximumUniqueSubarray([3,5,2,6,3,9,7,4])) #36

class UnitTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sol.maximumUniqueSubarray([]), 0)
        
    def test_valid1(self):
        self.assertEqual(sol.maximumUniqueSubarray([3,5,2,6,3,9,7,4]), 36)

if __name__ == "__main__":
    unittest.main()