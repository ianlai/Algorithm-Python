class Solution:
    
    '''
    2022/05/16
    BFS  [TC: O(MN): 51% / SC: O(MN): 39%]
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        print("Code2")
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        deq = collections.deque([(0, 0, 1)])
        distance = {(0, 0): 1}
        while deq: 
            x, y, d = deq.popleft()
            if x == m - 1 and y == n - 1:
                return d
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) == (0, 0):
                        continue
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] != 0:
                        continue
                    if (nx, ny) in distance:
                        continue
                    distance[(nx, ny)] = d + 1
                    deq.append((nx, ny, d + 1))
        return -1
    
    
    # BFS [O(n2): 75%]
    def shortestPathBinaryMatrix1(self, grid: List[List[int]]) -> int:
        print("Code1")
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1
        
        deq = collections.deque([(0, 0)])
        distances = collections.defaultdict(int)
        distances[(0, 0)] = 1
        while deq:
            p0, p1 = deq.popleft()
            for d0, d1 in [(0, 1), (0, -1), (1, 0), (-1,0 ), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                next_p0 = p0 + d0 
                next_p1 = p1 + d1
                if not (0 <= next_p0 < m and 0 <= next_p1 < n):
                    continue
                if grid[next_p0][next_p1] == 1:
                    continue
                if (next_p0, next_p1) in distances:
                    continue
                deq.append((next_p0, next_p1))
                distances[(next_p0, next_p1)] = distances[(p0, p1)] + 1
                if next_p0 == m - 1 and next_p1 == n - 1:
                    return distances[(next_p0, next_p1)]
        return -1       