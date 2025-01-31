class Solution:
    
    # 2022/01/25
    # DP + Heap [O(nlogn): 51%]
    def maxResult(self, nums: List[int], k: int) -> int:
        print("Code3")
        
        if not nums:
            return 0
        
        scores = [0] * len(nums)
        scores[0] = nums[0]
        hp = [(-nums[0], 0)]
        for i in range(1, len(nums)):
            while hp and i - hp[0][1] > k:
                heapq.heappop(hp)
            scores[i] = -hp[0][0] + nums[i]
            heapq.heappush(hp, (-scores[i], i))

        return scores[-1]
        
    # ===================================================   
    # DP + Monotonic Queue [Incorrect]
    def maxResult2(self, nums: List[int], k: int) -> int:
        print("Code2")
        
        if not nums:
            return 0
        
        res = nums[0]
        idx = 0
        deq = collections.deque([])
        for i in range(1, len(nums)):
            print(i, res, deq)
            
            while deq and i - deq[0][0] > k:
                print(" 1: pop left:", deq[0])
                popleft = deq.popleft()
                res += popleft[1]
                idx = popleft[0]
                
            while deq and nums[i] < deq[0][1]:
                print(" 2: pop left:", deq[-1])
                popleft = deq.popleft()
                res += popleft[1]
            deq.appendleft((i, nums[i])) 
            #deq.append((i, nums[i]))
        return res
    
    # ===================================================
    # DP [TLE]
    def maxResult1(self, nums: List[int], k: int) -> int:
        print("Code1")

        if not nums:
            return 0
        
        dp = [-inf] * len(nums)
        dp[0] = nums[0]
        
        for i in range(len(nums)):
            for j in range(i + 1, i + k + 1):
                if j == len(nums):
                    break
                dp[j] = max(dp[j], dp[i] + nums[j])
                
        return dp[-1]