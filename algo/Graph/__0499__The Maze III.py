class Solution:
    # [[0,0,0,0,0,0,0],[0,0,1,0,0,1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,1]]
    # [0,4]
    # [2,0]
    
    #     [[0,1,0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[1,0,0,1,0,0,0,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,1,0]]
    # [2,4]
    # [7,6]

    # Dijkstra varient (two condition) [54%]
    def findShortestWay(self, maze: List[List[int]], start: List[int], destination: List[int]) -> str:
        
        m, n = len(maze), len(maze[0])
        def findNextPositions(p):
            x, y = p[0], p[1]
            nextPositions = collections.defaultdict(tuple)
            
            isInserted = False
            for i in range(x, m, 1):
                if maze[i][y] == 1:
                    nextPositions[(i-1, y)] = (i - 1 - x, "d")
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(m-1, y)] = (m - 1 - x, "d")
            
            isInserted = False
            for i in range(x, -1, -1):
                if maze[i][y] == 1:
                    nextPositions[(i+1, y)] = (x - (i + 1), "u")
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(0, y)] = (x, "u")
                
            isInserted = False
            for j in range(y, n, 1):
                if maze[x][j] == 1:
                    nextPositions[(x, j-1)] = (j - 1 - y, "r")
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(x, n-1)] = (n - 1 - y, "r")
                
            isInserted = False
            for j in range(y, -1, -1):
                if maze[x][j] == 1:
                    nextPositions[(x, j+1)] = (y - (j + 1), "l")
                    isInserted = True
                    break
            if not isInserted:
                nextPositions[(x, 0)] = (y, "l")
            return nextPositions
        
        def isHoldBetween(cur, nxt):
            if cur[0] == nxt[0]:
                if destination[0] != cur[0]:
                    return -1
                if cur[1] <= destination[1] <= nxt[1]:
                    return abs(cur[1] - destination[1]) 
                if cur[1] >= destination[1] >= nxt[1]:
                    return abs(cur[1] - destination[1]) 
            elif cur[1] == nxt[1]:
                if destination[1] != cur[1]:
                    return -1
                if cur[0] <= destination[0] <= nxt[0]:
                    return abs(cur[0] - destination[0]) 
                if cur[0] >= destination[0] >= nxt[0]:
                    return abs(cur[0] - destination[0]) 
            else:
                print("Error")
            return -1
        
        heap = [(0, tuple(start))]
        distances = collections.defaultdict(lambda: inf)
        distances[tuple(start)] = 0
        directions = collections.defaultdict(str)
        res = []
        pathString = []
        while heap:
            d, cur = heapq.heappop(heap)
            #print("out:", cur, d, directions[cur])
            
            
            for nxt, (cost, direction) in findNextPositions(cur).items():
                #print("    in:", nxt, cost, direction)
                        
                if distances[cur] + cost < distances[nxt]: 
                    distances[nxt] = distances[cur] + cost
                    directions[nxt] = directions[cur] + direction
                    heapq.heappush(heap, (distances[nxt], nxt))
                
                if distances[cur] + cost == distances[nxt] and directions[cur] + direction < directions[nxt]:
                    distances[nxt] = distances[cur] + cost
                    directions[nxt] = directions[cur] + direction
                    heapq.heappush(heap, (distances[nxt], nxt))                    
                    
                lastStep = isHoldBetween(cur, nxt)
                if lastStep != -1:
                    totalStep = distances[cur] + lastStep
                    #print("   hole!", (directions[cur] + direction, totalStep))
                    pathString.append((directions[cur] + direction, totalStep))
                        
        res = sorted(pathString, key=lambda path: (path[1], path[0]))
        print(res)
        if len(res) != 0:
            return res[0][0]
        else:
            return "impossible"