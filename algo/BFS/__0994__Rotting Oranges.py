class Solution:
    
    # 2021/11/14
    # BFS [O(n2): 95%]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        #Find starting points 
        numOfOrange = 0 
        rottenOranges = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numOfOrange += 1
                elif grid[i][j] == 2:
                    rottenOranges.append((i,j))
                    numOfOrange += 1
        numOfRotton = len(rottenOranges)
        if numOfRotton == numOfOrange:
            return 0
        
        #BFS
        deq = collections.deque(rottenOranges)
        step = 0 
        while deq:
            for _ in range(len(deq)):
                i, j = deq.popleft()
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        deq.append((ni, nj))
                        numOfRotton += 1                        
            step += 1
        if numOfRotton == numOfOrange:
            return step - 1
        return -1
                    
    # =========================================
    
    # 2021/07/01
    def orangesRotting1(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        deq = collections.deque([])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    deq.append((i,j))
                    visited[i][j] = 1
        day = 0
        
        while deq:
            #print(day)
            #for i in range(m):
            #    print(grid[i], "  ", visited[i])
            #print(deq)
            for _ in range(len(deq)):
                (i, j) = deq.popleft()
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if visited[ni][nj] == 1:
                        continue
                    if grid[ni][nj] == 0:
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                    deq.append((ni, nj))
                    visited[ni][nj] = 1
            day += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        print("day:" , day)
        return max(0, day - 1)
        