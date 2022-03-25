import heapq

# ==============================================
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def add(self, val):
        if self.root:
            self._add(self.root, val)
        else:
            self.root = BSTNode(val)
            
    def _add(self, node, val):
        assert node is not None
        if val <= node.val:
            if node.left:
                self._add(node.left, val)
            else:
                node.left = BSTNode(val)
        else:
            if node.right:
                self._add(node.right, val)
            else:
                node.right = BSTNode(val)
        
    def findKth(self, k):
        if self.root is None:
            return None
        
        dummy = BSTNode(0)
        dummy.left = self.root
        stack = [dummy]
        
        for _ in range(k):
            if not stack:
                return None
            cur = stack.pop()
            if cur.left:
                cur = cur.left
                while cur:
                    stack.append(cur)
                    cur = cur.right
        return stack[-1].val
     
    #Debug 
    def print(self):
        inorder = []
        self._dfs(self.root, inorder)
        print(inorder)
        
    def dfs(self, node, arr):
        if node is None:
            return 
        self._dfs(node.left, arr)
        arr.append(node.val)
        self._dfs(node.right, arr)

        
#2022/03/25
#BST [TLE]
class KthLargest:
    
    #O(mlogm) [m is the initial number of element]
    def __init__(self, k: int, nums: List[int]):
        print("Code4")
        self.bst = BST()
        self.k = k
        for num in nums:
            self.bst.add(num)
        #bst.print()
    
    #Add: O(logn)
    #FindKth: O(logn + k)
    def add(self, val):
        self.bst.add(val)
        return self.bst.findKth(self.k)
    
# ==============================================
    
#2022/03/25
#Binary search and insert (like insertion sort) [39%]
class KthLargest3:
    
    #O(mlogm) [m is the initial number of element]
    def __init__(self, k: int, nums: List[int]):
        print("Code3")
        self.nums = sorted(nums)      
        self.k = k
    
    #O(n)
    def add(self, val):
        idx = bisect.bisect_left(self.nums, val)
        self.nums.insert(idx, val)
        return self.nums[len(self.nums)-self.k]
    
# ==============================================

#2021/06/14 
class KthLargest2:
    
    # First-k Min-Heap [Time: 89% / Space: 49%]
    # Heapify [O(k)]
    def __init__(self, k: int, nums: List[int]):
        print("Code2")
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
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class KthLargest1:
    # Sorted linkedlist [TLE]
    # Sort [O(n2)]
    def __init__(self, k: int, nums: List[int]):
        print("Code1")
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
    def add(self, val: int) -> int:
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