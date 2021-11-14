class Solution:
    
    #BFS [O(mn): 66%]
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        
        starts = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    starts.append((i, j))
        
        deq = collections.deque(starts)
        visited = [[0 for _ in range(n)] for _ in range(m)]
        while(deq):
            i, j = deq.popleft()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    if rooms[ni][nj] == -1:
                        continue
                    if rooms[ni][nj] == 0:
                        continue
                    rooms[ni][nj] = min(rooms[i][j] + 1, rooms[ni][nj])
                    
                    # visited means no more start
                    # but visited we should still update the val
                    if visited[ni][nj] == 0: 
                        deq.append((ni, nj))
                        visited[ni][nj] = 1 