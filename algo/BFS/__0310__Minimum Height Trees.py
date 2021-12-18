class Solution:
    
    # 2021/12/18
    # Topological-Sorting [O(n): 51%]
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        print("Code3")
        if len(edges) == 0:
            return [0]
        
        graph = collections.defaultdict(set)
        indegree = [0] * n
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            indegree[v1] += 1
            indegree[v2] += 1
            
        leaves = collections.deque([v for v in range(n) if indegree[v] == 1])
        while len(graph) > 2:  #Not using leaves
            for _ in range(len(leaves)):
                v = leaves.popleft()
                indegree[v] -= 1
                for nv in list(graph[v]):
                    indegree[nv] -= 1
                    if indegree[nv] == 1:
                        leaves.append(nv)
                    # Update graph
                    graph[v].remove(nv)
                    if len(graph[v]) == 0:
                        del graph[v]
                    graph[nv].remove(v)
                    if len(graph[nv]) == 0:
                        del graph [nv]
        return leaves
        
    # =============================================
    
    # 2021/12/17
    # Memoization + DFS [Incorrect] 
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        print("Code2")
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        print(graph)
        
        heightMatrix = [[None for _ in range(n)]for _ in range(n)]
        for v in range(n):
            visited = set([v])
            print("dfs:", v)
            self.dfs(graph, v, v, heightMatrix, visited, 0)
            for i, row in enumerate(heightMatrix):
                print(i, row)
            
        res = []
        return res
    
    def dfs(self, graph, start, v, heightMatrix, visited, layer):
        print(">> dfs", v)
        for nv in graph[v]:
            if nv in visited:
                continue
            visited.add(nv)
            if any(heightMatrix[nv]):
                for i in range(len(graph)):
                    if heightMatrix[nv][i] is None:
                        continue
                    if heightMatrix[start][i] is None: 
                        heightMatrix[start][i] = layer + heightMatrix[nv][i]
                    else:
                        heightMatrix[start][i] = min(heightMatrix[start][i], layer + heightMatrix[nv][i])
                continue
            heightMatrix[start][nv] = layer + 1
            self.dfs(graph, start, nv, heightMatrix, visited, layer + 1)
            
    # =============================================
    
    # 2021/12/17
    # N-time DFS [O(n2): TLE]
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        print("Code1")
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        nodeToHeight = {}
        minHeight = inf
        for v in range(n):
            visited = set([v])
            height = self.dfs1(graph, v, visited)
            minHeight = min(height, minHeight)
            nodeToHeight[v] = height
        # print(nodeToHeight)
        # print(minHeight)
        res = []
        for v in range(n):
            if nodeToHeight[v] == minHeight:
                res.append(v)
        return res
    
    def dfs1(self, graph, v, visited):
        height = 0
        for nv in graph[v]:
            if nv in visited:
                continue
            visited.add(nv)
            height = max(height, self.dfs1(graph, nv, visited) + 1)
        return height