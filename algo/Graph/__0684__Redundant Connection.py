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
        self.parents = [-1] * (n)  # 0 ~ n

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

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def union(self, x, y):
        if x not in self.parent:
            self._add_node(x)
        if y not in self.parent:
            self._add_node(y)

        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:  #union-by-rank
                self._union_root(rootX, rootY)
            else:
                self._union_root(rootY, rootX)
            return True #different set (union)
        return False #same set
        
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node]) #path compression
        return self.parent[node]

    def _add_node(self, node):
        assert node not in self.parent
        self.parent[node] = node
        self.rank[node] = 0

    def _union_root(self, root, node):
        self.parent[node] = root
        self.rank[root] = max(self.rank[root], self.rank[node] + 1)
 

class DSU8:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0 
        
    def find(self, x):
        if x in self.parent:
            if x == self.parent[x]:
                return x
            rx = self.find(self.parent[x])
            self.parent[x] = rx
            return rx
        else:
            self.parent[x] = x
            self.rank[x] = 0
            self.count += 1
            return x 
            
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
                self.rank[rx] = max(self.rank[ry], self.rank[rx] + 1)
            else:
                self.parent[ry] = rx
                self.rank[ry] = max(self.rank[rx], self.rank[ry] + 1)
            self.count -= 1
            return True  #可連接
        return False     #不可連接

class Solution:
    
    
    # 2022/05/10
    # Disjoint Set [O(E*a(V)) = O(E): 70% / O(V):6%]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print("Code8")
        dsu = DSU8()
        for v1, v2 in edges:
            if not dsu.union(v1, v2): #不可連接，因為本來就連著，是同一塊
                return [v1, v2]
                
        
    # 2022/05/10
    # DFS [O(VE): 33% / O(V):6%]
    def findRedundantConnection7(self, edges: List[List[int]]) -> List[int]:
        print("Code7")
        def dfs(v1, v2, visited):
            if v1 == v2:
                return True
            if v1 in visited:
                return False
            visited.add(v1)
            for nv in graph[v1]:
                if dfs(nv, v2, visited):
                    return True
                
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            visited = set()
            if dfs(v1, v2, visited): #加之前就到的了
                return [v1, v2]
            else: #加入這條邊
                graph[v1].add(v2)
                graph[v2].add(v1)
        return None
    
    # 2021/12/30
    # Union-Find, general class [O(): 16%]
    def findRedundantConnection6(self, edges: List[List[int]]) -> List[int]:
        print("Code6: UnionFind Class + General implementation (大神)")
        disjointSet = DisjointSet()
        for v1, v2 in edges:
            if not disjointSet.union(v1, v2):
                return [v1, v2]

    # =============================================       
    # 2021/12/07 
    # Union-Find [O(n2): 32%]
    def findRedundantConnection5(self, edges: List[List[int]]) -> List[int]:
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