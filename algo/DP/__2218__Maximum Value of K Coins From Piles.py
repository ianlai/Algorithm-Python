class Solution:
    
    # Memoization DP, loop through piles then min(pile[idx], k)
    # Use 2D memo to achieve memoization [O(p*k): 44% ~ TLE]
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        print("Code5")
        self.count = 0

        def dp(idx, k, memo):
            if k == 0:
                return 0
            if idx == len(piles):
                return 0 #coins are less than k
            if k in memo[idx]:
                return memo[idx][k]
            self.count += 1
            
            ##### Core (medium)  #####
            # Case 102/122 takes 785 ms 
            # https://leetcode.com/submissions/detail/668231965/testcase/
            cur = 0
            total = nextVal = dp(idx+1, k, memo)
            for i in range(min(len(piles[idx]), k)):
                cur += piles[idx][i]
                nextVal = dp(idx+1, k-i-1, memo)
                total = max(total, cur + nextVal)
            memo[idx][k] = total
            return total
        
        memo = collections.defaultdict(dict)
        res = dp(0, k, memo)
        print("self.count", self.count)
        return res 
    
    # ================================================
    
    # Memoization DP, loop through piles then min(pile[idx], k)
    # Use memo to achieve memoization [O(p*k): 22% ~ TLE]
    def maxValueOfCoins4(self, piles: List[List[int]], k: int) -> int:
        print("Code4")
        self.count = 0

        def dp(idx, k, memo):
            if k == 0:
                return 0
            if idx == len(piles):
                return 0 #coins are less than k
            if (idx, k) in memo:
                return memo[(idx, k)]
            self.count += 1
            
            ##### Core (medium)  #####
            # Case 102/122 takes 785 ms 
            # https://leetcode.com/submissions/detail/668231965/testcase/
            cur = 0
            total = nextVal = dp(idx+1, k, memo)
            for i in range(min(len(piles[idx]), k)):
                cur += piles[idx][i]
                nextVal = dp(idx+1, k-i-1, memo)
                total = max(total, cur + nextVal)
            memo[(idx, k)] = total
            return total
        
        memo = {}
        res = dp(0, k, memo)
        print("self.count", self.count)
        return res 
    
    # ================================================

    # Memoization DP, loop through piles then min(pile[idx], k)  [O(p*k): 22%]
    # Use lru_cache 
    def maxValueOfCoins3(self, piles: List[List[int]], k: int) -> int:
        print("Code3")
        self.count = 0
        @lru_cache(None)
        def dp(idx, k):
            if k == 0:
                return 0
            if idx == len(piles):
                return 0 #coins are less than k
            self.count += 1
            
            ##### Core (fast)  #####
            # Case 102/122 takes 460 ms 
            # https://leetcode.com/submissions/detail/668231965/testcase/
            cur = 0
            total = nextVal = dp(idx+1, k)
            for i in range(min(len(piles[idx]), k)):
                cur += piles[idx][i]
                nextVal = dp(idx+1, k-i-1)
                total = max(total, cur + nextVal)
            return total
        
        memo = {}
        res = dp(0, k)
        print("self.count", self.count)
        return res 
    
    # ================================================
    
    # Memoization DP, loop through piles then k [TLE] 
    def maxValueOfCoins2(self, piles: List[List[int]], k: int) -> int:
        print("Code2")
        self.count = 0
        @lru_cache(None)
        def dp(idx, k):
            if k == 0:
                return 0
            if idx == len(piles):
                return 0 #coins are less than k
            self.count += 1
            
            ##### Core (slow)  #####
            # Case 102/122 takes 5333 ms 
            # https://leetcode.com/submissions/detail/668231965/testcase/
            nextVal = dp(idx+1, k)
            total = cur = 0
            for i in range(k+1):
                if 0 < i <= len(piles[idx]):
                    cur += piles[idx][i-1]
                    nextVal = dp(idx+1, k-i)
                total = max(total, cur + nextVal)
            return total
        res = dp(0, k)
        print("self.count", self.count)
        return res 
    
    # ================================================
    # Memoization, memo the whole piles's status (very slow) [TLE]
    def maxValueOfCoins1(self, piles: List[List[int]], k: int) -> int:
        print("Code1")
        
        def dfs(indices, k, total, memo):
            #print(k, indices, total)
            if k == 0:
                return total 
            key = tuple(indices + [k])
            if key in memo:
                return memo[key]
            
            val = 0
            for ith, idx in enumerate(indices):
                if idx == len(piles[ith]):
                    continue
                indices[ith] = idx + 1
                val = max(val, dfs(indices, k-1, total + piles[ith][idx], memo))
                indices[ith] = idx
                
            memo[key] = val
            return val 

        indices = [0] * len(piles)
        memo = {}
        return dfs(indices, k, 0, memo)