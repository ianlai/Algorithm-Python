# https://leetcode.com/problems/01-matrix/submissions/
    
class Solution:
    
    # DP [O(mn): 65%]
    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        print("DP")
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        m, n = len(mat), len(mat[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)] 
        
        # Go Down and Right
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        
        # Go Top and Left 
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp

    # ===============================================================
    
    # BFS-2 (slightly faster than BFS-1) [O(mn): 33%]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        print("BFS-2")
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        
        m, n = len(mat), len(mat[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)] 
        deq = collections.deque([])
        
        # Initialize 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    deq.append((i, j, 0)) #i, j, val
        #BFS 
        while deq:
            i, j, val = deq.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] :
                if not ((0 <= ni < m) and (0 <= nj < n)):
                    continue
                if res[ni][nj] == float('inf'):
                    res[ni][nj] = val + 1 #not need to compare 
                    deq.append((ni, nj, res[ni][nj]))
        return res
    
    # ===============================================================
    
    # BFS-1 [O(mn): 14%]
    def updateMatrix1(self, mat: List[List[int]]) -> List[List[int]]:
        print("BFS-1")
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        
        m, n = len(mat), len(mat[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)] 
        deq = collections.deque([])
        
        # Initialize 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    deq.append((i, j))
        #BFS 
        while deq:
            i, j = deq.popleft()
            for (ni, nj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] :
                if not ((0 <= ni < m) and (0 <= nj < n)):
                    continue
                if res[ni][nj] != float('inf'):
                    continue
                    
                val = float('inf')
                for (nni, nnj) in [(ni+1, nj), (ni-1, nj), (ni, nj+1), (ni, nj-1)] :
                    if ((0 <= nni < m) and (0 <= nnj < n)):
                        val = min(val, res[nni][nnj])
                val += 1
                res[ni][nj] = val
                deq.append((ni, nj))
        return res
                