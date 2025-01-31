class MedianFinder:
    def __init__(self):
        self.lo = [] #max heap
        self.hi = [] #min heap
    
    # O(logn)
    def addNum(self, num):
        if self.lo and num <= -self.lo[0]:
            heapq.heappush(self.lo, -num)
        elif self.hi and num >= self.hi[0]:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -num)
            
        self.__balanceHeaps()
    
    # O(n)
    def removeNum(self, num):
        assert len(self.lo) + len(self.hi) > 0
        
        #O(n) faster [46%]
        def removeFromHeap(h, num):
            idx = h.index(num)
            h[idx] = h[-1]
            h.pop()
            if idx < len(h):
                heapq._siftup(h, idx)
                heapq._siftdown(h, 0, idx)
        
        #O(n) slower [30%]
        def removeFromHeap1(h, num):
            idx = h.index(num)
            h[idx] = h[-1]
            h.pop()
            heapq.heapify(h)

        if self.lo and num <= -self.lo[0]:
            removeFromHeap(self.lo, -num)
        elif self.hi and num >= self.hi[0]:
            removeFromHeap(self.hi, num)
            
        self.__balanceHeaps()
    
    # O(1)
    def findMedian(self):
        size = len(self.lo) + len(self.hi)
        if size % 2 == 0:
            return (-self.lo[0] + self.hi[0]) / 2
        else:
            return -self.lo[0]
    
    def __balanceHeaps(self):
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
    def __str__(self):
        return "lo:" + str([-v for v in self.lo]) + "  hi:" + str(self.hi)
  
class Solution:
    
    # 2022/03/21
    # Sliding Window + Two heap [46%]
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        print("Code2")
        if not nums:
            return []
        mf = MedianFinder()
        res = []
        for i, v in enumerate(nums):
            mf.addNum(v)
            #print(i, mf)
            if i < k - 1:
                continue
            median = mf.findMedian()
            res.append(median)
            mf.removeNum(nums[i-k+1])
        return res
    
    # ======================================================
    
    # 2022/02/05 
    # Sliding Window + Quick Select [TLE]
    def medianSlidingWindow1(self, nums: List[int], k: int) -> List[float]:
        print("Code1")
        if not nums:
            return []
        
        def findMedian(nums, start, end, k):
            mid = start + (end - start) // 2
            pivot = nums[mid] #MUST be static
            left, right = start, end 
            while left <= right:
                while left <= right and nums[left] < pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1 
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
            if k <= right:
                return findMedian(nums, start, right, k)
            if k >= left:
                return findMedian(nums, left, end, k)
            #print(start, end, nums, "->", nums[k])
            return nums[k]
            # if left == k:
            #     return nums[k]
            # elif left < k:
            #     findMedian(left, end, k)
            # else:
            #     findMedian(start, left, k)
        
        left = 0 
        res = []
        for right in range(len(nums)):
            if right - left + 1 >= k:
                arr = nums[left:right+1]
                if k % 2 == 1:
                    median = findMedian(arr, 0, len(arr) - 1, k//2)
                else:
                    m1 = findMedian(arr, 0, len(arr) - 1, k//2) 
                    m2 = findMedian(arr, 0, len(arr) - 1, k//2 - 1)
                    median = (m1 + m2) / 2
                res.append(median)
                left += 1
        return res