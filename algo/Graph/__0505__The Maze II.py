class Solution:
    
    # Dijkstra [O((mn)^2): 37%]
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        def findNextPositions(p):
            x, y = p[0], p[1]
            nextPositions = collections.defaultdict(int)
            
            isInserted = False
            for i in range(x, m, 1):
                if maze[i][y] == 1:
                    nextPositions[(i-1, y)] = i - 1 - x
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(m-1, y)] = m - 1 - x
            
            isInserted = False
            for i in range(x, -1, -1):
                if maze[i][y] == 1:
                    nextPositions[(i+1, y)] = x - (i + 1)
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(0, y)] = x
                
            isInserted = False
            for j in range(y, n, 1):
                if maze[x][j] == 1:
                    nextPositions[(x, j-1)] = j - 1 - y
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(x, n-1)] = n - 1 - y
                
            isInserted = False
            for j in range(y, -1, -1):
                if maze[x][j] == 1:
                    nextPositions[(x, j+1)] = y - (j + 1)
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(x, 0)] = y
            return nextPositions
        
        heap = [(0, tuple(start))]
        distances = collections.defaultdict(lambda: inf)
        distances[tuple(start)] = 0
        while heap:
            d, cur = heapq.heappop(heap)
            #print("out:", cur, d)
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return distances[cur]
            for nxt, cost in findNextPositions(cur).items():
                #print("    in:", nxt, cost)
                if distances[cur] + cost < distances[nxt]:
                    distances[nxt] = distances[cur] + cost
                    heapq.heappush(heap, (distances[nxt], nxt))
        return -1
                
                
                
        
        