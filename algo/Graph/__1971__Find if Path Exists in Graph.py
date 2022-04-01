class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        def dfs(g, cur, dest, visited):
            if cur == dest:
                return True
            if cur in visited:
                return False
            visited.add(cur)
            for nxt in g[cur]:
                if dfs(g, nxt, dest, visited):
                    return True
            return False
            
        visited = set()
        return dfs(graph, source, destination, visited)