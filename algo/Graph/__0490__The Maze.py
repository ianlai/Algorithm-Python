class Solution:
    
    # BFS [O(n): 29%]
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
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
            
        
        deque = collections.deque([start])
        visited = set()
        while deque:
            cur = deque.popleft()
            #print(cur)
            if cur[0] == destination[0] and cur[1] == destination[1]:
                return True
            for nxt, _ in findNextPositions(cur).items():
                if nxt in visited:
                    continue
                visited.add(nxt)
                deque.append(nxt)
        return False
                