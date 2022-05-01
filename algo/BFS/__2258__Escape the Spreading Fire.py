class Solution:
    
    # 2022/05/01
    # BFS + Binary Search 值域 [TC: O(mn + log(mn) * mn) = O(mnlog(mn)): 70% / SC: O(mn): 80%]
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def generateFireGrid():
            fireGrid = [[inf] * n for _ in range(m)]
            fires = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fires.append((i, j, 0))

            deq = collections.deque(fires)
            while deq:
                for _ in range(len(deq)):
                    x, y, t = deq.popleft()
                    fireGrid[x][y] = t 
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        if grid[nx][ny] == 2:
                            continue
                        if t+1 < fireGrid[nx][ny]:
                            deq.append((nx, ny, t+1))
            return fireGrid
        
        def checkSafe(waitTime, fireGrid):
            deq = collections.deque([(0, 0, waitTime)])
            visited = set()
            while deq:
                for _ in range(len(deq)):
                    x, y, t = deq.popleft()
                    if x == m-1 and y == n-1 and t <= fireGrid[x][y]:
                        return True
                    if t >= fireGrid[x][y]:
                        continue
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        if grid[nx][ny] == 2:
                            continue
                        deq.append((nx, ny, t+1))
            return False
        
        fireGrid = generateFireGrid()
        
        # Binary Search to check waiting time
        MAX_LIMIT = 2 * 10 ** 4 
        start, end = 0, MAX_LIMIT
        while start < end:
            mid = start + (end - start) // 2
            if checkSafe(mid, fireGrid):
                start = mid + 1
            else:
                end = mid

        #We can use start-1 to describe the two cases: out of left range and in range
        #Only the case out of right range needs to handle separately
        return start - 1 if start < MAX_LIMIT else 10 ** 9