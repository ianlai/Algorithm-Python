class Solution:
    
    # DFS [O(n): 45%]
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        def dfs(v, visited, subVisited):
            if v in subVisited:
                return 
            subVisited.add(v)
            visited.add(v)
            for nv in graph[v]:
                dfs(nv, visited, subVisited)
        
        #generate graph
        graph = collections.defaultdict(set)
        for v1, v2 in connections:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        #dfs 
        visited = set()
        numOfSub = 0
        for v in range(n):
            if v not in visited:
                subVisited = set()
                dfs(v, visited, subVisited)
                numOfSub += 1
        return numOfSub - 1 
                