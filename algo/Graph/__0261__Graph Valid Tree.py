class Solution:
    
    # Run DFS once ; passing prev into DFS func [O(E+V): 52%] 
    # O(E): contruct graph
    # O(V): DFS to traverse graph to find graph
    # Note: DFS takes O(V) because it will leave DFS if graph has circle, not reaching O(E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        print("Run DFS once")
        if len(edges) == 0:
            if n == 1:
                return True  #Tree
            else: 
                return False
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        def dfsFindCircle(graph, pre, cur, visited):
            for nxt in graph[cur]:
                if nxt == pre:
                    continue
                if nxt in visited:
                    return True
                visited.add(nxt)
                if dfsFindCircle(graph, cur, nxt, visited):
                    return True
            return False
        
        visited = set([edges[0][0]])
        if dfsFindCircle(graph, None, edges[0][0], visited):
            print("False: circle found")
            return False
        if n != len(visited):
            print("False: isolated node found", n, visited)
            return False
        
        return True
        

    # ==================================
    # DFS E times [O(EV): 5%]
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        print("Run DFS for every edge")
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