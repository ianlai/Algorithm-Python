class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node]) #Path Compression
            #return self.find(self.parent[node])  
            return self.parent[node]  
        return node
        
    def union(self, n1, n2):
        if n1 not in self.parent:
            self._addNode(n1)
        if n2 not in self.parent:
            self._addNode(n2)
        root1 = self.find(n1)
        root2 = self.find(n2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:  #Union by rank
                self._appendToRoot(root1, root2)
            else:
                self._appendToRoot(root2, root1)
            return True
        return False
        
    def _addNode(self, node):
        self.parent[node] = node
        self.rank[node] = 0 
        
    def _appendToRoot(self, root, node):
        self.parent[node] = root
        self.rank[root] = max(self.rank[root], self.rank[node] + 1)
        
class Solution:
    
    # 2021/12/30
    # Disjoint Set (general) [18%] //Improvement doesn't reflect, but just Leetcode sometimes run faster
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        print("Code4: General Disjoint Set")
        dset = DisjointSet()
        grid = [[0 for _ in range(n)] for _ in range(m)]
        res = []
        count = 0
        for i, j  in positions:
            if grid[i][j] == 1:
                res.append(count)
                continue
            grid[i][j] = 1 
            count += 1
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] != 1:
                    continue
                if dset.union((i, j) , (ni, nj)):
                    count -= 1
            res.append(count)
        return res
    
    # =========================================
    # 2021/12/07
    # Union-Find (2D) [5%]
    def numIslands23(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        print("Code3: UnionFind(2D)")
        
        grid = [[0 for _ in range(n)] for _ in range(m)]
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

        count = 0
        res = []
        for i, j in positions:
            if grid[i][j] == 1:  #originally
                res.append(res[-1])
                continue
                
            grid[i][j] = 1
            connectedCount = 0
            for ni, nj in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] != 1:
                    continue
                if union((i, j), (ni, nj)):
                    connectedCount += 1
            count += (1 - connectedCount)
            res.append(count)
            
            # TLE
            # islandSet = set()
            # for i in range(m):
            #     for j in range(n):
            #         if grid[i][j] == 1:
            #             islandSet.add(find((i, j)))
            # res.append(len(islandSet))
        return res
    
    # =========================================
    # 2021/11/21
    # Union-Find (2D) [5%]
    def numIslands22(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        print("Code2: UnionFind(2D)")
        
        grid = [[0 for _ in range(n)] for _ in range(m)]
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

        count = 0
        res = []
        for i, j in positions:
            if grid[i][j] == 1:  #originally
                res.append(res[-1])
                continue
                
            grid[i][j] = 1
            connectedCount = 0
            for ni, nj in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if grid[ni][nj] != 1:
                    continue
                if union((i, j), (ni, nj)):
                    connectedCount += 1
            count += (1 - connectedCount)
            res.append(count)
            
            # TLE
            # islandSet = set()
            # for i in range(m):
            #     for j in range(n):
            #         if grid[i][j] == 1:
            #             islandSet.add(find((i, j)))
            # res.append(len(islandSet))
        return res
    
    # =========================================
    # DFS [TLE]
    def numIslands2_DFS(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        print("Code1")
        if not m or not n:
            return []
        
        A = [[0 for _ in range(n)] for _ in range(m)]
        results = []
        idx = 0
        for i, j in positions:
            A[i][j] = 1
            #print(idx)
            results.append(self.getNumOfIsland(A))
            idx += 1
        return results

    def getNumOfIsland(self, A):
        # for row in A:
        #     print(row)
        m, n = len(A), len(A[0])
        count = 0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                if visited[i][j] == 1:
                    continue 
                #print(i, j)
                self.dfs(A, i, j, visited)
                count += 1
        #print("-------------")
        return count
            
    def dfs(self, A, i, j, visited):
        m, n = len(A), len(A[0])
        if not (0 <= i < m and 0 <= j < n):
            return 
        if visited[i][j] == 1:
            return 
        if A[i][j] == 0:
            return 
        visited[i][j] = 1
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            self.dfs(A, ni, nj, visited)