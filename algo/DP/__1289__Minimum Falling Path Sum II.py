class Solution:
    
    # DP + Heap [O(n*(nlogn+n)) = O(n2*logn): 38%]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
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
            for j in range(n):

                min1, min1Idx = heapq.heappop(h1)
                min2, min2Idx = h1[0]
                heapq.heappush(h1, (min1, min1Idx))
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