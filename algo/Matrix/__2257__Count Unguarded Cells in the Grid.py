class Solution:
    
    # Matrix traverse [O(4MN)=O(MN): 58% / O(MN): 75%]
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        count = m * n
        for x, y in guards:
            grid[x][y] = "g"
            count -= 1
            
        for x, y in walls:
            grid[x][y] = "w"
            count -= 1
            
        for i in range(m):
            for j in range(n):                    
                if grid[i][j] == "g":
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        ni, nj = i, j 
                        while True:
                            ni, nj = ni + di, nj + dj
                            if not (0 <= ni < m and 0 <= nj < n):
                                break
                            if grid[ni][nj] == "w":
                                break
                            if grid[ni][nj] == "g":
                                break
                            if grid[ni][nj] == 0:
                                grid[ni][nj] = 1
                                count -= 1
        return count
        