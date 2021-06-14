import heapq

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        
        
class KthLargest:
    
    # First-k Min-Heap [Time: 89% / Space: 49%]
    
    # Heapify [O(k)]
    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.nums = [] #[0] is min
        for num in nums:
            self.add(num)
            
    # Add [O(logk)] ; kthLargest [O(1)]
    def add(self, val):
        if len(self.nums) < self.capacity or val > self.nums[0]: 
            heapq.heappush(self.nums, val)
        if len(self.nums) > self.capacity:
            heapq.heappop(self.nums)
        return self.nums[0]
        
    
    # ==============================================

    # Sorted linkedlist [TLE]
    
    # Sort [O(n2)]
    def __init__3(self, k: int, nums: List[int]):
        self.k = k
        nums = sorted(nums)[::-1]
        self.preHead = Node()
        cur = self.preHead 
        for num in nums:  #descending 
            #print(num)
            newNode = Node(num)
            cur.next = newNode
            cur = cur.next
        #self.print()
        
    def print(self):
        cur = self.preHead.next
        #print("print", cur.val)
        while cur:
            print(cur.val, "->", end = "")
            cur = cur.next
        print()
        

    # Add [Real: O(idx of val in sorted array); Worst: O(n)]; kthLargest [O(k)]
    def add3(self, val: int) -> int:
        pre, cur = self.preHead, self.preHead.next
        while True:
            if not cur or val > cur.val:
                newNode = Node(val)
                pre.next = newNode
                newNode.next = cur
                break
            pre = pre.next
            cur = cur.next
        
        #self.print()
        
        count = 0 
        cur = self.preHead.next
        for _ in range(self.k - 1):
            cur = cur.next
        #print(cur.val)
        return cur.val
                
    
    # ==============================================
    # Sorted array [TLE]
    
    # Sort [O(n2)]
    def __init__2(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[::-1]  #descending 

    # Add [Real: O(n)] ; kthLargest [O(1)]
    def add2(self, val: int) -> int:
        #print(">>", val, self.nums)
        if len(self.nums) == 0 or val < self.nums[-1]:
            self.nums.append(val)
        else:    
            temp = self.nums[:]
            self.nums = []
            for i in range(len(temp)):
                if val < temp[i]:
                    self.nums.append(temp[i])
                else:
                    #print("append", val, " to ", self.nums)
                    self.nums.append(val)
                    self.nums.extend(temp[i:])
                    break
                    
        #print(val, self.nums)
        return self.nums[self.k - 1]         
            
    # ==============================================
    # Heap [TLE]
    
    # Heapify [O(n)]
    def __init__1(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    # Add [O(logn)] ; kthLargest[O(n) + O(k*logn)]
    def add1(self, val: inf) -> int:
        
        # Add O(logn)
        heapq.heappush(self.nums, val)
        
        # Space O(n)
        newHeap = self.nums[:]
        
        # Get O((n-k)*logn)
        for _ in range(len(newHeap) - self.k):
            heapq.heappop(newHeap)
            
        return newHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)