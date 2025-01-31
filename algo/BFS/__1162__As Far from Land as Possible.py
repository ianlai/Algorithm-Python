class Solution:
    
    # 2022/05/21
    # Multiple source BFS [O(MN):68% / O(MN):32%]
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        land = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append((i, j, 0))

        visited = [[False] * n for _ in range(m)]
        maxDistance = 0
        deq = collections.deque(land)
        while deq:
            x, y, d = deq.popleft()
            maxDistance = max(maxDistance, d)
            for nx, ny in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == 1:
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                deq.append((nx, ny, d+1))
        return maxDistance if maxDistance != 0 else -1