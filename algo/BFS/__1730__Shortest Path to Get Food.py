class Solution:
    
    # 2022/05/27
    # BFS [O(N): 50% / O(N): 11%]
    def getFood(self, grid: List[List[str]]) -> int:
        
        start = None
        isStartFound = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    start = (i, j)
                    isStartFound = True
                    break
            if isStartFound:
                break
            
        deq = collections.deque([start])
        layer = 0
        visited = set([start])
        
        while deq:
            for _ in range(len(deq)):
                x, y = deq.popleft()
                if grid[x][y] == "#":
                    return layer 
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                        continue
                    if grid[nx][ny] == "X":
                        continue
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    deq.append((nx, ny))
            layer += 1
        return -1