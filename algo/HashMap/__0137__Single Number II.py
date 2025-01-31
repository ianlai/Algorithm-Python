class Solution:
    
    # Use counter hashset [O(n): 64%, O(n): 56%]
    def singleNumber(self, nums: List[int]) -> int:
        numCounter = collections.Counter()
        for num in nums:
            numCounter[num] += 1
        for num, count in numCounter.items():
            if count == 1:
                return num