import heapq

class Heap:
    def __init__(self):
        self.heap = []
    def append(self, val):
        heapq.heappush(self.heap, -val)
    def pop(self):
        heapq.heappop(self.heap)
    def max(self):
        return -self.heap[0]
    
    # O(n) -> Index find O(n), heapify all nodes O(n)
    # def remove(self, val):
    #     idx = self.heap.index(-val)
    #     self.heap[idx] = self.heap[0]
    #     self.pop()
    #     heapq.heapify(self.heap)   
    
    # O(n) -> Index find O(n), sift of idx one node O(logn)
    def remove(self, val):
        idx = self.heap.index(-val)
        self.heap[idx] = self.heap[0]
        self.pop()
        #heapq.heapify(self.heap)   
        if idx < len(self.heap):
            heapq._siftup(self.heap, idx)
            heapq._siftdown(self.heap, 0, idx)

    def __str__(self):
        return str([-val for val in self.heap])  

class Solution:
    
    # 2022/02/04
    # Sliding window + Monotonic queue descending [O(n): 44%]
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        print("Code4")
        
        maxqueue = collections.deque()
        left = 0
        res = []
        for right in range(len(nums)):
            
            #Keep monotonic queue
            while maxqueue and nums[right] >= nums[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(right)
            
            #Sliding left pointer
            if right - left + 1 >= k:
                res.append(nums[maxqueue[0]])
                
                #Popleft max queue if left pointer pointed to the max
                if maxqueue and maxqueue[0] == left:
                    maxqueue.popleft()
                left += 1 
        return res
                
    # ===========================================

    # 2021/06/13
    # Deque [O(n) 87%, O(k), 85%]
    # (1) popright the useless values to keep window small
    # (2) store index to popleft the value when the window sliding out 
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        print("Code3")
        if not nums:
            return None
        
        dq = collections.deque([])
        results = []
        
        # No need he special case
        #if k == 1:
        #    return nums
        
        for i in range(len(nums)):
            cur = nums[i]
             # Remove small values before appending from right
            while dq and cur > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
                
            if i < k - 1: # Preparation 
                continue
            else:
                # Remove old values until find one still valid 
                while dq[0] < i - k + 1:
                    dq.popleft()
                    
                # Get max
                results.append(nums[dq[0]])
                
        return results
                
    # ===========================================
    # Deque [ERROR]
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        print("Code2")
        if not nums:
            return None
        dq = collections.deque([])
        results = []
        
        if k == 1:
            return nums
        
        for i in range(len(nums)):
            cur = nums[i]
            print(i)
            if i < k:
                dq.append(cur)
                while cur > dq[0]:
                    dq.popleft()
            else: 
                results.append(dq[0])
                dq.append(cur)
                while cur > dq[0] or len(dq) > k:
                    dq.popleft()
            print(dq, results)
        results.append(dq[0])
        return results
            
    # ===========================================   
    # Heap + Deque [O(n2) TLE]
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        print("Code1")
        if not nums:
            return None
        
        pq = Heap()
        dq = collections.deque([])
        results = []
        
        for i in range(len(nums)):
            if i < k:
                # print(i, "pre")
                pq.append(nums[i])
                dq.append(nums[i])
                # print(pq)
                # print(dq)
            else: 
                # print(i, "start")
                results.append(pq.max())
                pq.append(nums[i])
                dq.append(nums[i])
                head = dq.popleft()
                pq.remove(head)
                # print(pq, pq.max())
                # print(dq)       
                
            #print("-----------")
        results.append(pq.max())
        return results