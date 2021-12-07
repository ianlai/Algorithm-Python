class DSU():
    def __init__(self):
        self.par = list(range(1001))
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution1():
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge

class UnionFind4:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)  # 0 ~ n

    #Improvement1: Path compression
    def find(self, i):
        #print("Find:", i)
        if self.parents[i] < 0:
            return i
        #return self.find(self.parents[i])  #No path compression
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i1, i2):
        head1 = self.find(i1)
        head2 = self.find(i2)
        if head1 != head2:
            self.parents[head1] = head2

            
class UnionFind5:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)  # 0 ~ n

    #Improvement1: Path compression
    def find(self, i):
        if self.parents[i] < 0:
            return i 
        self.parents[i]  = self.find(self.parents[i])
        return self.parents[i] 

    #Improvement2: Union by rank
    def union(self, i1, i2):
        head1 = self.find(i1)
        head2 = self.find(i2)
        rank1 = -self.parents[head1]
        rank2 = -self.parents[head2]
        if head1 == head2:
            return False
        else:
            rank = rank1 + rank2
            #2 connects to 1 
            if rank1 >= rank2:
                self.parents[head2] = head1
                self.parents[head1] = -rank 
            #1 connects to 2
            else:
                self.parents[head1] = head2
                self.parents[head2] = -rank 
            return True
            
class Solution:
    
    # 2021/12/07 
    # Union-Find [O(n2): 32%]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print("Code5: UnionFind Class + Improvement")
        if not edges:
            return []
        
        nodes = set()
        for edge in edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
        
        uf = UnionFind5(len(nodes))        
        for v1, v2 in edges:
            if not uf.union(v1, v2):
                return [v1, v2]
            
    # =============================================       
    # 2021/12/07 
    # Union-Find [O(n2): 32% ]
    def findRedundantConnection4(self, edges: List[List[int]]) -> List[int]:
        print("Code4 - UnionFind Class")
        if not edges:
            return []
        
        nodes = set()
        for edge in edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
        
        uf = UnionFind4(len(nodes))
        
        for v1, v2 in edges:
            #print(uf.parents)
            if uf.find(v1) != uf.find(v2):
                uf.union(v1, v2)
            else:
                return [v1, v2]
            
    # =============================================        
    
    # 2021/11/21  (WIP)
    # Union-Find [O(n2), 75% -> (Path Compression) 89% -> (Union by Rank) ?? ]
    def findRedundantConnection3(self, edges: List[List[int]]) -> List[int]:
        print("Code3 - UnionFind")
        
        nodes = set([])
        for edge in edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
            
        parents = [-1] * (len(nodes) + 1)  # 0 ~ n
        
        if not edges:
            return []
        
        #Original
        # def find(parents, i):
        #     if parents[i] == -1:
        #         return i
        #     return find(parents, parents[i])

        #Improvement1: Path compression
        def find(parents, i):
            if parents[i] == -1:
                return i
            parents[i] = find(parents, parents[i])
            return parents[i]

        def union(parents, i1, i2):
            head1 = find(parents, i1)
            head2 = find(parents, i2)
            if head1 != head2:
                parents[head1] = head2
        
        for edge in edges:
            if find(parents, edge[0]) != find(parents, edge[1]):
                union(parents, edge[0], edge[1])
                #print(parents)
            else:
                return edge
    
    # =============================================
    # 2021/11/15
    # DFS [O(VE): 38%]
    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        print("Code2 - DFS")
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
        print("Code1 - UnionFind")
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
    
    def find(self, parents, i):
        if parents[i] == -1:
            return i
        return self.find(parents, parents[i])
    
    def union(self, parents, i1, i2):
        head1 = self.find(parents, i1)
        head2 = self.find(parents, i2)
        if head1 != head2:
            parents[head1] = head2