class Solution:
    
    # DFS + Memoization [O(mnmn): 5% / O(mn): 92%]
    # 
    # Naive DFS [TLE]
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        self.maxSize = 0
        
        def dfs(x, y, visited, memo):
            #self.maxSize = max(self.maxSize, len(visited))
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            maxLength = 1
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                if (nx, ny) in visited:
                    continue
                
                visited.add((nx, ny))
                maxLength = max(maxLength, 1 + dfs(nx, ny, visited, memo))
                visited.remove((nx, ny))
                
            memo[(x, y)] = maxLength
            return maxLength
    
        totalMaxLength = 0
        for i in range(m):
            for j in range(n):
                visited = set()
                visited.add((i, j))
                memo = {}
                #memo[(i, j)] = 1
                thisMaxLength = dfs(i, j, visited, memo)
                #print(i, j, thisMaxLength)
                totalMaxLength = max(totalMaxLength, thisMaxLength)
    
        return totalMaxLength