# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

MAX = 2 ** 31 - 1
class Solution:
    
    # Exponential Backoff, then Binary Search [O(logn): 75%]
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        upper = 0
        for x in range(1, 32):
            num = reader.get(2 ** x)
            #print(x, 2 ** x, num)
            if num == target:
                return 2 ** x
            elif num > target:
                upper = x
                break
        
        print("Upper:", upper)
        
        start, end = 0, 2 ** upper
        while start < end:
            mid = start + (end - start) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                end = mid
        # if reader.get(start) == target:
        #     return start
        return -1
        
        