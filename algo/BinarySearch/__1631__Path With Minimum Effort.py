class Solution:
    
    # 2022/04/28
    # Binary Search + DFS [O(log(10^6) * MN): 22% / O(MN): 8%]
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        print("Code2")
        m, n = len(heights), len(heights[0])
        
        def dfs(x, y, limit, visited):
            if x == m-1 and y == n-1:
                return True
            
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                diff = abs(heights[nx][ny] - heights[x][y])
                if diff > limit:
                    continue
                    
                visited.add((nx, ny))  #no backtracking 
                if dfs(nx, ny, limit, visited):
                    return True
            return False 
        
        def hasPath(limit):
            visited = set()
            visited.add((0, 0))
            return dfs(0, 0, limit, visited)
        
        start, end = 0, 10 ** 6 
        while start < end:
            mid = start + (end - start) // 2
            if hasPath(mid):
                end = mid
            else:
                start = mid + 1
        return start 
    
    # ==========================================================
    
    # DFS [TLE: 3^(mn) / mn]
    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        print("Code1")
        m, n = len(heights), len(heights[0])
        
        self.minDiff = inf
        def dfs(row, col, cur, diff, visited):
            if row == m-1 and col == n-1:
                if diff < self.minDiff:
                    self.minDiff = diff
                return 
            
            # if not (0 <= row < len(heights) and 0 <= col < len(heights[0])):
            #     return 
            # if (row, col) in visited:
            #     return 

            for ni, nj in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:                
                if not (0 <= ni < len(heights) and 0 <= nj < len(heights[0])):
                    continue 
                if (ni, nj) in visited:
                    continue 
                #cur.append([ni, nj])
                visited.add((ni, nj))
                curDiff = abs(heights[ni][nj] - heights[row][col])
                dfs(ni, nj, cur, max(diff, curDiff), visited)
                visited.remove((ni, nj))
                #cur.remove([ni, nj])
            return 
        
        visited = set()
        visited.add((0,0))
        dfs(0, 0, [], 0, visited)
        return self.minDiff