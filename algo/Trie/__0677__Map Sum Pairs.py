class Node:
    def __init__(self):
        self.cmap = collections.defaultdict(Node)
        self.val = 0

# 2022/03/27
# Trie [83%]
class MapSum:

    def __init__(self):
        self.root = Node()
        
    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            node = node.cmap[ch]
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            node = node.cmap[ch]
        res = self._sum(node)
        return res
    
    def _sum(self, node) -> int:
        if node is None:
            return 0
        res = node.val
        for ch, next_node in node.cmap.items():
            res += self._sum(next_node)
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)