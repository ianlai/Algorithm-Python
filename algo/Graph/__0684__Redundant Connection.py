class Solution:
    
    # 2021/11/15
    # DFS [O(VE): 38%]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print("DFS")
        self.graph = collections.defaultdict(list)
        for v1, v2 in edges:
            visited = set()
            if self.dfs(v1, v2, visited):
                return [v1, v2]
            else:
                self.graph[v1].append(v2)
                self.graph[v2].append(v1)
        return []
        
    def dfs(self, v1, v2, visited):
        if v1 == v2:
            return True
        if v1 in visited:
            return 
        visited.add(v1)
        for n1 in self.graph[v1]:
            if self.dfs(n1, v2, visited):
                return True
        return False
        
    # =============================================
    # 2021/07/07
    # Union-Find [O(n2), 47%]
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        print("Union-Find")
        if not edges:
            return []
        
        nodes = set([])
        for edge in edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
            
        parents = [-1] * (len(nodes) + 1)  # 0 ~ n
        
        for edge in edges:
            if self.find(parents, edge[0]) != self.find(parents, edge[1]):
                self.union(parents, edge[0], edge[1])
            else:
                return edge
            #print(parents)
            #print()
    
    def find(self, parents, i):
        if parents[i] == -1:
            return i
        return self.find(parents, parents[i])
    
    def union(self, parents, i1, i2):
        head1 = self.find(parents, i1)
        head2 = self.find(parents, i2)
        if head1 != head2:
            parents[head1] = self.find(parents, head2)