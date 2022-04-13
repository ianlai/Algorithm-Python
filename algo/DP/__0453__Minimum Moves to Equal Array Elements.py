class Solution:
    
    # 2022/04/13
    # Sort + DP [O(nlogn): 68%]
    def minMoves(self, nums: List[int]) -> int:
        print("Code3")
        
        nums.sort()
        count = 0
        accum = 0
        diff = 0
        for i in range(1, len(nums)):
            accum += diff
            diff = nums[i] - nums[i-1]
            count += diff + accum
        return count
        
    # Math [O(n): 93%]
    def minMoves2(self, nums: List[int]) -> int:
        print("Code2")
        count = 0
        minNum = min(nums)
        for v in nums:
            count += (v - minNum)
        return count
        
    # Heap [TLE]
    def minMoves1(self, nums: List[int]) -> int:
        print("Code1")
        maxHeap = [-v for v in nums]
        heapq.heapify(maxHeap)
        count = 0
        while min(maxHeap) != max(maxHeap):
            pop = heapq.heappop(maxHeap)
            pop2 = maxHeap[0]
            #print(maxHeap, pop, pop2)
            diff = max(1, pop2-pop)
            heapq.heappush(maxHeap, pop + diff)
            count += diff
        return count