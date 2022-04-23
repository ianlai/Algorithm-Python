class Solution:
    
    # Post-order DFS in graph [O(n): 87% / O(h): 13%]
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def generateTree(edges):
            graph = collections.defaultdict(set)
            for v1, v2 in edges:
                graph[v1].add(v2)
                graph[v2].add(v1)
            return graph
        
        def dfs(graph, visited, cur):
            count = 0
            for nxt in graph[cur]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                count += dfs(graph, visited, nxt)
                visited.remove(nxt)
            
            if count != 0 or hasApple[cur]:
                return count + 2
            return 0
            
        graph = generateTree(edges)
        visited = set([0])
        res = dfs(graph, visited, 0) 
        return res - 2 if res != 0 else 0