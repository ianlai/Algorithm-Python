class Solution:
    
    # DFS from edge [O((2N+2M)*MN): 55%]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pMat = [[0 for _ in range(n)] for _ in range(m)]
        aMat = [[0 for _ in range(n)] for _ in range(m)]
        
        # Traverse from the edge of Pacific Ocean 
        for i in range(m):
            self.dfs(heights, pMat, i, 0)
        for j in range(n):
            self.dfs(heights, pMat, 0, j)
        
        # Traverse from the edge of Atlantic Ocean 
        for i in range(m):
            self.dfs(heights, aMat, i, n-1)
        for j in range(n):
            self.dfs(heights, aMat, m-1, j,)
        
        # Form the res list
        ans = []
        for i in range(m):
            for j in range(n):
                if pMat[i][j] and aMat[i][j]:
                    ans.append([i, j])
        return ans
            
        
    def dfs(self, ht, mat, i, j):
        m, n = len(ht), len(ht[0])
        if not (0 <= i < m and 0 <= j < n):
            return 
        
        mat[i][j] = 1
        
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= ni < m and 0 <= nj < n):
                continue 
            if ht[ni][nj] < ht[i][j]:
                continue
            if mat[ni][nj] == 1:
                continue
            mat[ni][nj] = 1
            self.dfs(ht, mat, ni, nj)
