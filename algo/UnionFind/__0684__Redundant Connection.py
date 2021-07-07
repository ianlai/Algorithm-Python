class Solution:
    
    # Union-Find [O(n2), 47%]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        nodes = set([])
        for edge in edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
            
        parents = [-1] * (len(nodes) + 1)  # 0 ~ n
        
        for edge in edges:
            #print(edge)
            #print(self.find(parents, edge[0]), self.find(parents, edge[1]))
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