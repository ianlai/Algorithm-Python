class Solution:
    
    # DFS on Graph [O(V+E) / 53%]
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
            
        graphMap = self.buildGraph(edges)
        print(graphMap)
        count = self.countGraph(n, graphMap)
        return count 
    
    def buildGraph(self, edges):
        graphMap = {}
        for n1, n2 in edges:
            if n1 not in graphMap:
                graphMap[n1] = []
            if n2 not in graphMap:
                graphMap[n2] = []
            graphMap[n1].append(n2)
            graphMap[n2].append(n1)
        return graphMap
    
    def countGraph(self, n, graphMap):
        visited = set([])
        count = 0
        for i in range(n):
            if i not in graphMap:  #node is not in edges 
                count += 1 
                continue
                
            if i in visited:
                continue
            count += 1
            visited.add(i)
            self.traverseDfs(i, graphMap, visited)
            #print(visited)
        return count 
    
    def traverseDfs(self, src, graphMap, visited):
        # if src in visited:
        #     return 
        
        for dest in graphMap[src]:
            if dest in visited:
                continue 
            visited.add(dest)
            self.traverseDfs(dest, graphMap, visited)
        
            