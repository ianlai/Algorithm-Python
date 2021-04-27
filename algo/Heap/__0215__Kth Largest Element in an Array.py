import heapq

class Solution:
    
    # Use Min Heap [95%, O(k + (n-k)log(k)) -> O(k + nlogk)]  
    # To form a k-size heap with the largest elements inside 
    # Assuming n = 10000000, k = 100, log(n) = 8 
    # Complexity = 100 + 10000000 * 2
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
    
    # Get k max [13%, O(nk)]
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        print("Get k max")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        for i in range(k):
            m = max(nums)
            nums.remove(m)
        return m
    
    # Sorting [86%, O(nlogn)]
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        print("Sorting")
        if not nums or len(nums) == 0 or k <= 0 or k > len(nums):
            return None 
        nums = sorted(nums)[::-1]
        return nums[k-1]
    
    
