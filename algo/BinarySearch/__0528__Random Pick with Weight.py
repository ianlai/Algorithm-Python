class Solution:

    
    # [1, 5, 2] => 
    # [1, 6, 8]
    #  0-1
    #  1-2-3-4-5-6
    #  6-7-8
    
    # Binary Search [O(logn): 79%]
    def __init__(self, w: List[int]):
        self.prefixSum = []
        for i, v in enumerate(w):
            if i == 0:
                self.prefixSum.append(w[i])
            else:
                self.prefixSum.append(w[i] + self.prefixSum[-1])

    def pickIndex(self) -> int:
        p = self.prefixSum
        if not p:
            return -1
        target = random.random() * p[-1]
        start, end = 0, len(p)
        while start < end:
            mid = start + (end - start) // 2
            if p[mid] == target:
                return mid
            elif p[mid] < target:
                start = mid + 1
            else:
                end = mid 
        return start
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()