class Solution:
    
    # 2022/06/01
    # Path search (backtracking) [O(3*MN): 19% / O(MN + MN): 88%]
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def dfs(path, visited):
            i, j = path[-1]
            curNode = grid[i][j]
            nextNodes = 0
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] == 0:
                    continue
                if (ni, nj) in visited:
                    continue
                visited.add((ni, nj))
                nextNodes = max(nextNodes, dfs(path + [(ni, nj)], visited))
                visited.remove((ni, nj))
            res = curNode + nextNodes
            return res
           
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                visited = set([(i, j)])
                res = max(res, dfs([(i, j)], visited))
        return res