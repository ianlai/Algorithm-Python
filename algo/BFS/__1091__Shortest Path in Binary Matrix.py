class Solution:
    
    # BFS [O(n2): 75%]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
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