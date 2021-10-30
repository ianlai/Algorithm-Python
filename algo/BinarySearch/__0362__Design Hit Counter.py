class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.arr.append(timestamp)

    # Linear [O(n): 17%]
    def getHits1(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        target = timestamp - 300
        if len(self.arr) == 0:
            return 0

        firstIdx = None
        for i, e in enumerate(self.arr):
            if e > target:
                firstIdx = i
                break
        if firstIdx is None:
            return 0
        return len(self.arr) - firstIdx
    
    # Binary Search [O(logn): 76%]
    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        if len(self.arr) == 0:
            return 0
        
        start, end = 0, len(self.arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.arr[mid] == target:  #until find the last target
                start = mid
            elif self.arr[mid] > target:
                end = mid
            else:
                start = mid
                
        #print(self.arr)
        #print(start, " t:", target, end, end = "")
        count = 0
        if target < self.arr[start]: 
            count = len(self.arr) - start
        elif target == self.arr[start]:  
            count = len(self.arr) - start - 1
        elif target == self.arr[end]:   
            count = len(self.arr) - end - 1
        elif target > self.arr[end]:   
            count = 0
        else:
            count = len(self.arr) - end    
        #print(" -> ", count)
        return count 



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)