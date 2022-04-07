class Solution:
    
    # 2022/04/07
    # DFS [O(V+E): 93%]
    # Note: confirm again about the vertex and edge 
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
        
        def dfs(source, cur, destination, visited):
            if cur == destination:
                if len(graph[cur]) == 0:
                    visited[cur] = True
                    return True
                else:
                    visited[cur] = False
                    return False
            if cur not in graph:
                return False
            if cur in visited: 
                #return False
                return visited[cur]
            
            visited[cur] = False
            for nxt in graph[cur]:
                if not dfs(source, nxt, destination, visited):
                    return False
            visited[cur] = True
            return True
            
        visited = dict()
        return dfs(source, source, destination, visited)
        