class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            if n == 1:
                return True
            else:
                return False
            
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            visited = set([v1])
            if self.findCircle(graph, v1, v2, visited):
                #print("Circle")
                return False 
            graph[v1].add(v2)
            graph[v2].add(v1)
    
        #Traverse all 
        self.findCircle(graph, v1, -1, visited)
        if len(visited) == n:
            return True
        #print("Unconnected")
        return False
        
    def findCircle(self, graph, v1, target, visited):
        if v1 == target:
            return True
        for v in graph[v1]:
            if v in visited:
                continue
            visited.add(v)
            if self.findCircle(graph, v, target, visited):
                return True
        return False