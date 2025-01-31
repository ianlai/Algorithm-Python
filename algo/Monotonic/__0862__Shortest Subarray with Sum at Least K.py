class Solution:
    
    # 2022/01/22
    # Prefix sum + Monotonic Stack [O(n): 19%]
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        print("Code3")
        if not nums:
            return -1
        
        #Calculate preSum: O(n)
        #preSum = [0]
        #for v in nums:
        #    preSum.append(preSum[-1] + v)
        
        #Calculate presum + update monotonic queue together: O(n)
        preSum = 0
        res = inf
        deq = collections.deque([(-1, 0)]) #idx, preSum
        for i, v in enumerate(nums):
            preSum += v
            if v >= 0:      
                while deq and preSum - deq[0][1] >= k:
                    res = min(res, i - deq[0][0])
                    deq.popleft()  
            else:
                while deq and deq[-1][1] >= preSum:
                    deq.pop()
            deq.append([i, preSum])
        return res if res != inf else -1
    
    # ===========================================================

    # 2022/01/22
    # Traverse of prefix sum [O(n2): TLE]
    def shortestSubarray2(self, nums: List[int], k: int) -> int:
        print("Code2")
        if not nums:
            return -1
        preSum = [0]
        for v in nums:
            preSum.append(preSum[-1] + v)
        #print(preSum)
        
        res = inf
        for i in range(len(preSum)):
            for j in range(i+1, len(preSum)):
                curSum = preSum[j] - preSum[i]
                if curSum >= k:
                    res = min(res, j - i)
        return res if res != inf else -1
                    
    # ===========================================================
        
    # Sliding-Window (can only handle positive number) [Incorrect]
    def shortestSubarray1(self, nums: List[int], k: int) -> int:
        print("Code1")
        if not nums:
            return -1
        
        i = 0
        curSum = 0
        res = inf
        for j, v in enumerate(nums):
            curSum += v
            while curSum >= k:
                res = min(res, j - i + 1)
                curSum -= nums[i]
                i += 1
        return res if res != inf else -1