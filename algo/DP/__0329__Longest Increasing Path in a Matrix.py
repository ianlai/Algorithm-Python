class Solution:
    
    # 2022/05/19
    '''
    DP + Topological Sorting 
    TC: O(MN + MN)
    SC: O(MN + MN)
    '''
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m)]
        indegreeMap = collections.defaultdict(int)
        deq = collections.deque()
        
        for i in range(m):
            for j in range(n):
                indegree = 0
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if A[ni][nj] < A[i][j]:
                        indegree += 1
                indegreeMap[(i, j)] = indegree
                if indegree == 0:
                    deq.append((i, j))
                    dp[i][j] = 1
        while deq: 
            i, j = deq.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if A[ni][nj] > A[i][j]:
                    indegreeMap[(ni, nj)] -= 1
                    if indegreeMap[(ni, nj)] == 0:
                        deq.append((ni, nj))         
                        dp[ni][nj] = dp[i][j] + 1
        res = 0
        for row in dp:
            res = max(res, max(row))
        return res
        
    # 2022/04/30
    # DP + Topological Sorting [TC: O(MN): 44% / SC: O(MN+4MN+MN) = O(MN): 5%]
    def longestIncreasingPath5(self, matrix: List[List[int]]) -> int:
        print("Code5 - DP + Topological Sorting")
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # Form indegreeMap and graph
        indegreeMap = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        for i in range(m):
            for j in range(n):
                indegree = 0 
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if matrix[i][j] > matrix[ni][nj]:
                        indegree += 1
                    if matrix[i][j] < matrix[ni][nj]:
                        graph[(i, j)].add((ni, nj))
                indegreeMap[(i, j)] = indegree
        
        # Insert the 0-indegree points to deque
        deq = collections.deque()
        for i in range(m):
            for j in range(n):
                if indegreeMap[(i, j)] == 0:
                    deq.append((i, j, 1))
                    
        # Topological sorting 
        while deq:
            x, y, val = deq.popleft()
            dp[x][y] = val
            for nx, ny in graph[(x, y)]:
                indegreeMap[(nx, ny)] -= 1
                if indegreeMap[(nx, ny)] == 0:
                    deq.append((nx, ny, val+1))

        res = 0
        for row in dp:
            res = max(res, max(row))
        return res
            
        
    # ==================================================

    # 2022/04/29
    # DFS + Memoization (lru_cache) [O(V+E) = O(MN + 4MN) = O(MN): 85% / O(MN): 15%]
    def longestIncreasingPath4(self, matrix: List[List[int]]) -> int:
        print("Code4 - DFS + Memoization")
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(None)
        def dfs(x, y):
            maxLength = 1
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                maxLength = max(maxLength, 1 + dfs(nx, ny))
            return maxLength
    
        totalMaxLength = 0
        for i in range(m):
            for j in range(n):
                totalMaxLength = max(totalMaxLength, dfs(i, j))
    
        return totalMaxLength
    
    # ==================================================

    # DFS + Memoization (memo, removed visited, memo reused) [O(MN): 39% / O(MN): 55%]
    def longestIncreasingPath3(self, matrix: List[List[int]]) -> int:
        print("Code3")
        m, n = len(matrix), len(matrix[0])
        
        def dfs(x, y, memo):
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            maxLength = 1
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                #if (nx, ny) in visited:
                #   continue
                
                #visited.add((nx, ny))
                maxLength = max(maxLength, 1 + dfs(nx, ny, memo))
                #visited.remove((nx, ny))
                
            memo[(x, y)] = maxLength
            return maxLength
    
        totalMaxLength = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                thisMaxLength = dfs(i, j, memo)
                totalMaxLength = max(totalMaxLength, thisMaxLength)
    
        return totalMaxLength
    
    # ==================================================

    # DFS + Memoization (with visited) [O(mnmn): 5% / O(mn): 92%]
    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        print("x Code2")
        m, n = len(matrix), len(matrix[0])
        
        def dfs(x, y, visited, memo):
            
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
                thisMaxLength = dfs(i, j, visited, {})
                totalMaxLength = max(totalMaxLength, thisMaxLength)
    
        return totalMaxLength
    
    # ==================================================
    
    # Naive DFS [TLE]
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        print("x Code1")    
        m, n = len(matrix), len(matrix[0])
        self.maxSize = 0
        
        def dfs(x, y, visited):
            self.maxSize = max(self.maxSize, len(visited))
            
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                dfs(nx, ny, visited)
                visited.remove((nx, ny))
        
        for i in range(m):
            for j in range(n):
                visited = set()
                visited.add((i, j))
                dfs(i, j, visited) 
    
        return self.maxSize