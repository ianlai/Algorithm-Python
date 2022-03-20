# 2022/03/20
# Two heaps [86%]
class MedianFinder:
    def __init__(self):
        print("Code4")
        self.maxheap = [] #small part
        self.minheap = [] #large part
        self.size = 0

    #O(logn)
    def addNum(self, num: int) -> None:
        
        if self.maxheap and num < self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        elif self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
    
        #Balance from small part to large part
        while len(self.maxheap) > len(self.minheap) + 1: #allow small part more than 1 (easier for findMedian)
            pop = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -pop)
        
        #Balance from large part to small part 
        while len(self.minheap) > len(self.maxheap):
            pop = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -pop)
            
    #O(1)
    def findMedian(self) -> float:
        #print(self.maxheap, self.minheap)
        size = len(self.maxheap) + len(self.minheap)
        if size % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0] #since small part always one element more 

# ==========================================
# 2022/03/20    
# Insertion sort (linear search)  [TLE]
class MedianFinder3:
    def __init__(self):
        print("Code3")
        self.arr = []

    # O(n)
    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return 
        for i in range(len(self.arr)):
            if i == 0:
                continue
            if self.arr[i-1] <= num <= self.arr[i]:
                self.arr.insert(i, num)
                return
        if num <= self.arr[0]:
            self.arr.insert(0, num)
        elif num >= self.arr[-1]: 
            self.arr.append(num)
        else:
            print("ERROR")
        return 
      
    # O(1)
    def findMedian(self) -> float:
        #print(self.arr)
        size = len(self.arr)
        if size % 2 == 0:
            return (self.arr[size//2] + self.arr[size//2-1]) / 2  
        else:
            return self.arr[size//2]

# ==========================================
# 2022/03/20
# Sorting [TLE]
class MedianFinder2:
    def __init__(self):
        print("Code2")
        self.arr = []

    # O(nlogn)
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    # O(1)
    def findMedian(self) -> float:
        size = len(self.arr)
        if size % 2 == 0:
            return (self.arr[size//2] + self.arr[size//2-1]) / 2  
        else:
            return self.arr[size//2]

# ==========================================
# 2022/03/20     
# Quick select to find median [TLE]
class MedianFinder1:

    def __init__(self):
        print("Code1")
        self.arr = []

    # O(1)
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
    # O(nlogn) / worst case O(n2)
    def findMedian(self) -> float:
        m = 0
        if len(self.arr) % 2 == 0:
            m1 = self.getTopK(0, len(self.arr)-1, (len(self.arr) // 2))
            m2 = self.getTopK(0, len(self.arr)-1, (len(self.arr) // 2 - 1))
            m = (m1 + m2) / 2
        else:
            m = self.getTopK(0, len(self.arr)-1, len(self.arr) // 2)
        return m
            
    def getTopK(self, start, end, k) -> int:
        mid = start + (end - start) // 2 
        pivot = self.arr[mid]
        l, r = start, end 
        while l <= r: 
            while l <= r and self.arr[l] < pivot:
                l += 1
            while l <= r and self.arr[r] > pivot:
                r -= 1
            if l <= r:
                self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
                l += 1
                r -= 1
        if k >= l:
            return self.getTopK(l, end, k)
        elif k <= r:
            return self.getTopK(start, r, k)
        else:
            return self.arr[k]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()