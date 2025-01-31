class Solution:
    
    # Binary Search [O(MlogM) M is the largest element in nums: 50%]
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) > threshold:
            return -1
        
        def findMinIndex(nums, threshold, left, right):
            start, end = left, right
            while start < end:
                mid = start + (end - start) // 2
                if isGreater(nums, threshold, mid):
                    start = mid + 1
                else:
                    end = mid
            return start
                    
        def isGreater(nums, threshold, divisor):
            val = 0
            for num in nums:
                val += ceil(num / divisor)
            res = val > threshold 
            #print(divisor, val, res)
            return res
        
        maxVal = max(nums)
        return findMinIndex(nums, threshold, 1, maxVal + 1)