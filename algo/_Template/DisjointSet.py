'''
Find        - TC: O(a(N)) ~= O(1)  #with Path Compression
Union       - TC: O(a(N)) ~= O(1)  #with Union by Rank
DisjointSet - SC: O(N)
'''
class DisjointSet:
    def __init__(self):
        self.count = 0
        self.parent = {}
        self.rank = {} #代表高度，不是個數！

    #找不到就做新的，指向自己(包含新增功能)
    #找的到就追到root，同時一路改成指向root。
    def find(self, x):
        # add new
        if x not in self.parent:
            self.count += 1
            self.parent[x] = x
            self.rank[x] = 0 #0或1都可以 (0代表是真的高度，一顆的時候就沒有高度)
            return x

        # find
        if x != self.parent[x]:
            # optimized-1: path compression
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        else:
            return x

    #小的接大的
    #可把判斷是否相同也包起來
    #運算都在root上，不是x,y上 否則根本沒效果！
    def union(self, x, y): 
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.count -= 1
            # optimized-2: union by rank (attach small to big)
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry  # attach rx to ry
                self.rank[ry] = max(self.rank[ry], self.rank[rx] + 1)
            else:
                self.parent[ry] = rx #attach ry to rx
                self.rank[rx] = max(self.rank[rx], self.rank[ry] + 1)

    def print(self):
        print("count:", self.count)
        for node in self.parent.keys():
            root = self.find(node)
            print(str(node) + "->" + str(root) + " (rank = " + str(self.rank[node]) + ")")

if __name__ == "__main__":
    print("Main of DisjointSet")

dj = DisjointSet()
dj.find(1)
dj.find(2)
dj.union(2, 3)
dj.union(3, 4)
dj.find(5)
dj.union(6, 7)
dj.union(6, 3)

dj.print()


