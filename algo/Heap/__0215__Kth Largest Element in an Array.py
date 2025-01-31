import heapq

class Solution:
    
    # Heap [25% / 18%]
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print("2022/06/22 - Python Syntax")
        return heapq.nlargest(k, nums)[-1]  #heap + sort

    # Quick Select [T.C. = O(n): 98% / S.C. = O(logn): 12%]
    # Avg T.C.   = O(n)    
    # Worst T.C. = O(n^2) 
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        print("2022/06/22 - Quick Select")
        def quickSelect(start, end, idx):
            mid = start + (end - start) // 2
            pivot = nums[mid]
            l, r = start, end
            while l <= r:
                while l <= r and nums[l] < pivot:
                    l += 1
                while l <= r and nums[r] > pivot: 
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            if idx >= l:
                return quickSelect(l, end, idx)
            elif idx <= r:
                return quickSelect(start, r, idx)
            return nums[idx]
        return quickSelect(0, len(nums) - 1, len(nums) - k)
    
    # Min Heap [O(k + (n-k)logk) / O(k)]
    # Max Heap [O(n + klogn)     / O(n)]
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        print("2022/06/22 - Max Heap")
        maxNums = [-x for x in nums]
        heapq.heapify(maxNums)
        for _ in range(k):
            m = heapq.heappop(maxNums)
        return -m
    
    # Sorting [O(nlogn): 38% / O(logn): 18%]
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        print("2022/06/22 - Sort")
        return sorted(nums, key = lambda x: -x)[k-1]
        
    
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        def partition(nums, k, start, end):
            #if start == end:
            #    return nums[k]
            
            pivotIdx = start + (end - start) // 2
            pivot = nums[pivotIdx]
            print("S:", start, "E:", end)
            print(nums, pivot)
            l, r = start, end
            while l <= r:
                while l <= r and nums[l] < pivot:
                    l += 1
                while l <= r and nums[r] > pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]    
                    l += 1
                    r -= 1
            # if l < k-1:
            #     return partition(nums, k, l, end)
            # if l > k-1:
            #     return partition(nums, k, start, r)
            # if l == k-1:
            #     return nums[l] 
            
            print(" R:", r, "L:", l)
            print(" ", nums)
            
            # r, l might has diff 1 or 2 
            if k <= r:
                return partition(nums, k, start, r)
            elif k >= l:
                return partition(nums, k, l, end)
            return nums[k]
            
        if not nums or not (0 < k <= len(nums)):
            return 0
        
        s, e = 0, len(nums) - 1
        print("Find {}-th ({} index)".format(len(nums) - k + 1, len(nums) - k))
        print(sorted(nums))
        print(nums)
        return partition(nums, len(nums) - k, s, e)
        
        
        
        

    
    # Quick Select [Avg: O(N), Worst: O(n2), 86%]
    # Quick Sort but only deal with one interval every time
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        print("Quick select")
        if not nums or k <= 0 or k > len(nums):
            return None
        #print("====" , sorted(nums), "====")
        
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)
                
    def partition2(self, nums, start, end, kIdx):
        if start == end:
            return nums[kIdx]

        left, right = start, end
        mid = left + (right - left) // 2 
        pivot = nums[mid]
        #print(">>>> partition:", nums, left, right, "pivot:", pivot)

        while left <= right: 
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if kIdx <= right:
            return self.partition(nums, start, right, kIdx) #left interval 
        if kIdx >= left:
            return self.partition(nums, left, end, kIdx) #right interval
        return nums[kIdx]

    # ==========================================================
    
    # Use Min Heap [95%, O(k + (n-k)log(k)) -> O(k + nlogk)]  
    # To form a k-size heap with the largest elements inside 
    # Assuming n = 10000000, k = 100, log(n) = 8 
    # Complexity = 100 + 10000000 * 2
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        print("Use min heap")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        
        heapNum = nums[:k]  #k size
        heapq.heapify(heapNum)
        for i in range(k, len(nums)):
            minimum = heapNum[0]
            if nums[i] > minimum:
                heapq.heappop(heapNum)           #remove the min in heapNum
                heapq.heappush(heapNum, nums[i]) #add a new element to heapNum since it's larger than previous min 
                
        return heapNum[0] #min in k-size heap (heap contains the largest k elements)
    
    # ==========================================================
    
    # Use Max Heap [45%, O(n + klog(n))  -> O(n + klogn)]
    # Assuming n = 10000000, k = 100, log(n) = 8 
    # Complexity = 10000000 + 100 * 8
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        print("Use max heap")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        
        negativeNums = [-x for x in nums]  #n size
        heapq.heapify(negativeNums)
        for i in range(k):
            m = heapq.heappop(negativeNums)
        return -m
    
    # ==========================================================
    
    # Get k max [13%, O(nk)]
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        print("Get k max")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        for i in range(k):
            m = max(nums)
            nums.remove(m)
        return m
    
    # ==========================================================
    
    # Sorting [O(nlogn), 86%, ]
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        print("Sorting")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        nums = sorted(nums)[::-1]
        return nums[k-1]