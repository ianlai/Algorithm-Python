class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        # add new
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x

        # find
        if x != self.parent[x]:
            # optimized-1: path compression
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        else:
            return x

    def union(self, x, y):
        '''
            Function of union
        '''
        # optimized-2: union by rank (attach small to big)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y  # attach x to y
            self.rank[y] = max(self.rank[y], self.rank[x] + 1)
        else:
            self.parent[y] = x #attach y to x
            self.rank[x] = max(self.rank[x], self.rank[y] + 1)
        

if __name__ == "__main__":
    print("Main of DisjointSet")
