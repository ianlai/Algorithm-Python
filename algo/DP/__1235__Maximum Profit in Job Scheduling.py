class Solution:
    
    # Sorting + DP (n1) + Binary Search 
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        print("Code4")
        p = []
        n = len(startTime)
        for i in range(len(startTime)):
            p.append([startTime[i], endTime[i], profit[i]])
        p.sort(key = lambda x: x[1])
        dp = [0] * n
        dp[0] = p[0][2]
        
        def findLast(p, idx):
            target = p[idx][0]
            start, end = 0, idx
            while start < end:
                mid = start + (end - start) // 2
                if p[mid][1] <= target:
                    start = mid + 1
                else:
                    end = mid
            return start - 1
                    
            
        for i in range(len(dp)):
            pstart = p[i][0]
            lastIdx = findLast(p, i,)
            dp[i] = max(dp[lastIdx] + p[i][2], dp[i-1])
        return dp[n-1]
    
    # ===================================================
    # Sorting + Memoization (n2) + Binary Search [TLE]
    def jobScheduling3(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        print("Code3")
        
        p = []
        for i in range(len(startTime)):
            p.append([startTime[i], endTime[i], profit[i]])
        p.sort(key = lambda x: x[0])
        #print(p)
        
        #Binary Search 
        def findNext(p, cur, lastEnd):
            start, end = cur + 1, len(p)
            while start < end:
                mid = start + (end - start) // 2
                if p[mid][0] < lastEnd:
                    start = mid + 1
                else:
                    end = mid 
            return start
        
        def dfs(p, idx, lastEnd, memo):
            if idx >= len(p):
                return 0
            if (idx, lastEnd) in memo:
                return memo[(idx, lastEnd)]
            
            # use
            nextIdx = findNext(p, idx, p[idx][1])
            res1 = p[idx][2] + dfs(p, nextIdx, p[idx][1], memo)
            
            # not use
            res2 = dfs(p, idx + 1, lastEnd, memo)
            
            res = max(res1, res2)
            memo[(idx, lastEnd)] = res
            return res
        
        memo = {}
        return dfs(p, 0, 0, memo)
    
    # ==================================================
    # Sorting + Memoization + Binary Search [TLE]
    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        print("Code2")
        
        p = []
        for i in range(len(startTime)):
            p.append([startTime[i], endTime[i], profit[i]])
        p.sort(key = lambda x: x[0])
        #print(p)
        
        #Binary Search 
        def findNext(p, cur, lastEnd):
            start, end = cur + 1, len(p)
            while start < end:
                mid = start + (end - start) // 2
                if p[mid][0] < lastEnd:
                    start = mid + 1
                else:
                    end = mid 
            return start
        
        def dfs(p, cur, lastEnd, memo):
            if cur >= len(p):
                return 0
            if (cur, lastEnd) in memo:
                return memo[(cur, lastEnd)]
            
            # use
            start = findNext(p, cur, p[cur][1])
            #print("cur:", cur, "lastEnd:", lastEnd, "start:", start)
            res1 = p[cur][2] + dfs(p, start, p[cur][1], memo)
            
            # not use
            res2 = dfs(p, cur + 1, lastEnd, memo)
            
            res = max(res1, res2)
            #print("cur:", cur, "res:", res1, res2)
            memo[(cur, lastEnd)] = res
            return res
        
        memo = {}
        return dfs(p, 0, 0, memo)
    
    # ==================================================
    # Sorting + Memoization [TLE]
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        print("Code1")
        
        p = []
        for i in range(len(startTime)):
            p.append([startTime[i], endTime[i], profit[i]])
        p.sort(key = lambda x: x[0])

        def dfs(p, cur, lastEnd, memo):
            if cur == len(p):
                return 0
            
            if (cur, lastEnd) in memo:
                return memo[(cur, lastEnd)]
            
            if p[cur][0] < lastEnd:
                res = dfs(p, cur + 1, lastEnd, memo)
            else:
                res = max(p[cur][2] + dfs(p, cur + 1, p[cur][1], memo), dfs(p, cur + 1, lastEnd, memo))
            
            memo[(cur, lastEnd)] = res
            return res
        
        memo = {}
        return dfs(p, 0, 0, memo)