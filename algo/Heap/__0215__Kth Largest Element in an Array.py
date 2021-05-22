import heapq

class Solution:
    
    # Quick Select [Avg: O(N), Worst: O(n2), 86%]
    # Quick Sort but only deal with one interval every time
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print("Quick select")
        if not nums or k <= 0 or k > len(nums):
            return None
        #print("====" , sorted(nums), "====")
        
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)
                
    def partition(self, nums, start, end, kIdx):
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