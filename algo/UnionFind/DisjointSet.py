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
      if self.rank[rootX] < self.rank[rootY]:
        self._union_root(rootX, rootY)
      else:
        self._union_root(rootY, rootX)
        
  def find(self, node):
    if self.parent[node] != node:
      self.parent[node] = self.find(self.parent[node])
    return self.parent[node]
    
  def _add_node(self, node):
    assert node not in self.parent
    self.parent[node] = node
    self.rank[node] = 0
    
  def _union_root(self, root, node):
    self.parent[node] = root
    self.rank[root] = max(self.rank[root], self.rank[node] + 1)

    