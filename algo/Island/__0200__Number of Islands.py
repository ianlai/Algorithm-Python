
class DisjointSet:
    def __init__(self):
        self.parent = {} 
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if x != self.parent[x]:
            return self.find(self.parent[x])
        else:
            return x
    def union(self, x, y):
        self.parent[y] = x # y attached to x 
        #self.parent[x] = y # x attached to y (won't work if we find cur only once)

class DisjointSetOptimized:
    def __init__(self):
        self.parent = {} 
        self.rank = {}
    def find(self, x):
        # add new
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        # find 
        if x != self.parent[x]:
            #optimized-1: path compression
            self.parent[x] = self.find(self.parent[x]) 
            return self.parent[x]
        else:
            return x
    def union(self, x, y):    
        #optimized-2: union by rank (attach small to big)
        if self.rank[x] < self.rank[y]: 
            self.parent[x] = y #attach x to y
            self.rank[y] = max(self.rank[y], self.rank[x] + 1)
        else:
            self.parent[y] = x #attach y to x
            self.rank[x] = max(self.rank[x], self.rank[y] + 1)
    
class Solution:
    
    # 2022/03/06
    # Union-Find; create Disjoint-Set class (optimized) [O(): 58%]
    def numIslands(self, grid: List[List[str]]) -> int:
        print("Code-7")
        dset = DisjointSetOptimized()
        islandCount = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                
                # Add new land 
                islandCount += 1
                
                # Traverse Up and Left neighbors (4 directions also fine but slower)
                for ni, nj in [(i, j-1), (i-1, j)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == "0":
                        continue
                    rootCur = dset.find((i, j))
                    rootNeightbor = dset.find((ni, nj))
                    if rootCur != rootNeightbor:
                        dset.union(rootCur, rootNeightbor)
                        islandCount -= 1
        return islandCount

    # ========================================
    
    # 2022/03/06
    # Union-Find; create Disjoint-Set class (simple) [O(): 30%]
    def numIslands6(self, grid: List[List[str]]) -> int:
        print("Code-6")
        dset = DisjointSet()
        islandCount = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                
                ### Add new land 
                islandCount += 1
                #we can find rootCur only once if we use rootCur as the root to union 
                #if we change to "self.parent[x] = y", then we need to put this line in for loop 
                rootCur = dset.find((i, j))  
                
                ### Traverse Up and Left neighbors (4 directions also fine but slower)
                for ni, nj in [(i, j-1), (i-1, j)]:
                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == "0":
                        continue
                    
                    rootNeightbor = dset.find((ni, nj))
                    if rootCur != rootNeightbor:
                        dset.union(rootCur, rootNeightbor)
                        islandCount -= 1
        return islandCount
                    
    # ========================================
    
    # 2021/11/21
    # Union-Find (2D) [5%]
    def numIslands5(self, grid: List[List[str]]) -> int:
        print("Code-5")
        
        m, n = len(grid), len(grid[0])
        parents = [[(-1, -1) for _ in range(n)] for _ in range(m)]
        
        def find(t):
            i, j = t[0], t[1]
            if parents[i][j] != (-1, -1):
                return find(parents[i][j])
            return t
            
        def union(t1, t2):
            root1 = find(t1)
            root2 = find(t2)
            if root1 != root2:
                i, j = root2[0], root2[1]
                parents[i][j] = root1
                return True #new
            return False #connected originally

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for ni, nj in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                        if not (0 <= ni < m and 0 <= nj < n):
                            continue
                        if grid[ni][nj] != "1":
                            continue
                        union((i, j), (ni, nj))
                            
        islandSet = set()  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islandSet.add(find((i, j)))
        
        return len(islandSet)
    
    # ========================================

    # 2021/11/21
    # Union-Find (2D) [12%]
    def numIslands4(self, grid: List[List[str]]) -> int:
        print("Code-4")
        
        m, n = len(grid), len(grid[0])
        size = m * n 
        parents = [[(-1, -1) for _ in range(n)] for _ in range(m)]
        roots = [[(-1, -1) for _ in range(n)] for _ in range(m)]
        
        def find(t):
            i, j = t[0], t[1]
            if parents[i][j] != (-1, -1):
                return find(parents[i][j])
            return t
            
        def union(t1, t2):
            root1 = find(t1)
            root2 = find(t2)
            #print("union:", t1, t2, " root:", root1, root2, end = "")
            if root1 != root2:
                i, j = root2[0], root2[1]
                parents[i][j] = root1
                #print(" O")
                return True #new
            #print(" X")
            return False #connected originally
        
        islands = []  #incorrect
        for i in range(m):
            for j in range(n):
                cur = (i, j)
                if grid[i][j] == "1":
                    isNewIsland = True
                    if 0 <= i - 1 < m and grid[i - 1][j] == "1":
                        pre = (i - 1, j)
                        if not union(cur, pre):
                            isNewIsland = False
                            
                    if 0 <= j - 1 < n and grid[i][j - 1] == "1": 
                        pre = (i, j - 1)
                        if not union(cur, pre):
                            isNewIsland = False
                    
                    if 0 <= i + 1 < m and grid[i + 1][j] == "1":
                        pre = (i + 1, j)
                        if not union(cur, pre):
                            isNewIsland = False
                            
                    if 0 <= j + 1 < n and grid[i][j + 1] == "1": 
                        pre = (i, j + 1)
                        if not union(cur, pre):
                            isNewIsland = False
                    
                    #incorrect, the connection status might change latter
                    if isNewIsland:
                        islands.append(cur) 
        
        islandSet = set()  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    roots[i][j] = "xxxx"
                    continue
                val = find((i, j))
                roots[i][j] = val
                islandSet.add(roots[i][j])
        
        # print("Parents:")
        # for row in parents:
        #     print(row)   
        # print("Roots:")
        # for row in roots:
        #     print(row)
        return len(islandSet)
        
    # ========================================

    # (1) Traversal: BFS
    # (2) Status: change grid to 0 after traversal
    # [O(m*n) / O(m*n) -> 56% / 35%]
    def numIslands3(self, grid: List[List[str]]) -> int:
        print("Code-3")
        print("BFS + change grid to 0 after traversal")
        if not grid or not grid[0]:
            return 0
        
        #visited = set()
        self.count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    #visited.add((i, j))
                    self.bfs(grid, i, j)
        return self.count 
                    
    def bfs(self, grid, i, j):
        self.count += 1 
        deq = collections.deque([(i, j)])
        #print(i, j)
        while deq:
            cur = deq.popleft()
            for d in [(1, 0), (-1,0), (0, 1), (0,-1)]:
                nextI = cur[0] + d[0]
                nextJ = cur[1] + d[1]
                # if (nextI, nextJ) in visited:
                #     continue
                if not(0 <= nextI < len(grid) and 0 <= nextJ < len(grid[0])):
                    continue
                if grid[nextI][nextJ] != "1":
                    continue
                grid[nextI][nextJ] = "0"
                #print(deq)
                #visited.add((nextI, nextJ))
                deq.append((nextI, nextJ)) 
                
    # ========================================
    # (1) Traversal: BFS
    # (2) Status: use visited set
    # [O(m*n) / O(m*n) -> 39% / 13%]
    def numIslands2(self, grid: List[List[str]]) -> int:
        print("Code-2")
        print("BFS + use visited set")
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        self.count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    self.bfs2(grid, i, j, visited)
        return self.count 
                    
    def bfs2(self, grid, i, j, visited):
        self.count += 1 
        deq = collections.deque([(i, j)])
        #print(i, j)
        while deq:
            
            cur = deq.popleft()
            for d in [(1, 0), (-1,0), (0, 1), (0,-1)]:
                nextI = cur[0] + d[0]
                nextJ = cur[1] + d[1]
                if (nextI, nextJ) in visited:
                    continue
                if not(0 <= nextI < len(grid) and 0 <= nextJ < len(grid[0])):
                    continue
                if grid[nextI][nextJ] != "1":
                    continue
                #print(deq)
                visited.add((nextI, nextJ))
                deq.append((nextI, nextJ))
                                
    # ========================================
    # (1) Traversal: DFS
    # (2) Status: change 1 to 0 after visited 
    # [O(m*n): 82%]
    def numIslands1(self, grid: List[List[str]]) -> int:
        print("Code-1")
        if grid is None or len(grid) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs1(grid, i, j)
        return count

    
    def dfs1(self, grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return
            
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs1(grid, i+1, j)
            self.dfs1(grid, i-1, j)
            self.dfs1(grid, i, j+1)
            self.dfs1(grid, i, j-1)