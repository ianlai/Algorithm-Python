class Solution:
    
    # DP + Record two mins [O(n2): 74%]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        print("Code-3: DP + Two Mins")
        n = len(matrix)
        
        # Init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # DP 
        for i in range(1, n):
            # Find 1st and 2nd smallest in row i 
            min1Val = min(dp[i-1])
            min1Idx = dp[i-1].index(min1Val)
            min2Val = inf
            if dp[i-1][:min1Idx]:
                min2Val = min(dp[i-1][:min1Idx]) 
            if dp[i-1][min1Idx+1:]:
                min2Val = min(min2Val, min(dp[i-1][min1Idx+1:]))
            
            # Inner loop
            for j in range(n):
                minVal = min1Val
                if j == min1Idx:
                    minVal = min2Val
                dp[i][j] = minVal + matrix[i][j]
        return min(dp[n-1])
    
    # ==============================================================

    
    # DP + Heap [O(n*(nlogn+n)) = O(n2*logn): 53%]
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        print("Code-2: DP + Heap")
        n = len(matrix)
        
        # init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        h1 = []
        for j in range(n):
            dp[0][j] = matrix[0][j]
            heapq.heappush(h1, (dp[0][j], j))
        
        # dp 
        for i in range(1, n):
            h2 = []
            min1, min1Idx = heapq.heappop(h1)
            min2, min2Idx = h1[0]
            heapq.heappush(h1, (min1, min1Idx))
            for j in range(n):
                if min1Idx != j:
                    minVal = min1
                else:
                    minVal = min2
                dp[i][j] = minVal + matrix[i][j]
                heapq.heappush(h2, (dp[i][j], j))
            h1 = h2
        return min(dp[n-1])
    
    # ==============================================================
    
    # DP [O(n3): 25%]
    def minFallingPathSum1(self, matrix: List[List[int]]) -> int:
        print("Code-1: DP")
        n = len(matrix)
        
        # init 
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        # dp 
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j+1:])
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][:j])
                else:
                    dp[i][j] = min(min(dp[i-1][j+1:]), min(dp[i-1][:j]))
                    
                dp[i][j] += matrix[i][j]

        return min(dp[n-1])