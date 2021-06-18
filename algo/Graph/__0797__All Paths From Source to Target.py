class Solution:
    
    # DFS on Graph, backtracking [O(2^E), 31%]
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph or not graph[0]:
            return []
        
        visited = set([])
        n = len(graph)
        result = []
        self.traverse(graph, n, 0, [0], result, visited)
        return result
        
    def traverse(self, graph, n, node, cur, result, visited):
        if node == n - 1:
            result.append(cur)
            return 
        
        for nextNode in graph[node]:
            if nextNode in visited: 
                continue
            visited.add(nextNode)
            self.traverse(graph, n, nextNode, cur + [nextNode], result, visited)
            visited.remove(nextNode)