class Solution:
    
    # 2022/02/03
    # Sliding window + two monotonic deque [O(n): 61%]
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        print("Code3")
        if not nums:
            return 0
        
        self.maxdeque = collections.deque()
        self.mindeque = collections.deque()
        def diff():
            return nums[self.maxdeque[0]] - nums[self.mindeque[0]]
            
        res = 0
        left = 0
        for right in range(len(nums)):
            while self.maxdeque and nums[self.maxdeque[-1]] < nums[right]:
                self.maxdeque.pop()
            self.maxdeque.append(right)
            
            while self.mindeque and nums[self.mindeque[-1]] > nums[right]:
                self.mindeque.pop()
            self.mindeque.append(right)
            
            # while left <= right and diff() > limit:
            if diff() > limit:  #NOT using while (lazy update)

                if self.maxdeque and left == self.maxdeque[0]:
                    self.maxdeque.popleft()
                if self.mindeque and left == self.mindeque[0]:
                    self.mindeque.popleft()
                left += 1
            #res = max(res, self.maxdeque[-1] - self.mindeque[0] + 1, self.mindeque[-1] - self.maxdeque[0] + 1)
            res = len(nums) - left
        return res
    
    # =============================================
    
    # 2022/02/03
    # Sliding window + deque + max/min func [O(n2): TLE]
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        print("Code2")
        if not nums:
            return 0
        
        self.arr = collections.deque()
        def diff():
            return max(self.arr) - min(self.arr)
        res = 0
        left = 0
        for right in range(len(nums)):
            self.arr.append(nums[right])
            while diff() > limit:
                left += 1
                self.arr.popleft()
            res = max(res, right - left + 1)
        return res
    
    # =============================================
    
    # 2022/02/03
    # Sliding window + list + max/min func [O(n2): TLE]
    def longestSubarray1(self, nums: List[int], limit: int) -> int:
        print("Code1")
        if not nums:
            return 0
        
        self.arr = []
        def diff():
            return max(self.arr) - min(self.arr)
        res = 0
        left = 0
        for right in range(len(nums)):
            self.arr.append(nums[right])
            while diff() > limit:
                left += 1
                self.arr.pop(0)
            res = max(res, right - left + 1)
        return res
            
            
            