class Node:
    def __init__(self):
        self.chmap = collections.defaultdict(Node)
        self.value = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    # Always ok to insert (do the check outside)
    def insert(self, arr, value):
        #print("Insert:", arr, value)
        node = self.root
        for folder in arr:
            node = node.chmap[folder]
        node.value = value
        
    def search(self, arr):
        #print("search:", arr)
        node = self.root
        for folder in arr:
            if folder in node.chmap:
                node = node.chmap[folder]
            else:
                return False, -1
        return True, node.value
    
    
    # 2022/03/14 
    # Use Trie to check parent and current paths [73%]
class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        wholePath = path.split("/")[1:]
        #print("createPath: ", wholePath)
        
        #Check the path existed; if existed, then return False
        existed, val = self.trie.search(wholePath)
        if existed:
            return False
        
        #Check the parent path existed; if not existed, then return False
        existed, val = self.trie.search(wholePath[:-1])
        if not existed:
            return False
        
        self.trie.insert(wholePath, value)
        return True
        
    def get(self, path: str) -> int:
        wholePath = path.split("/")[1:]
        #print("get: ", wholePath)
        _, resInt = self.trie.search(wholePath)
        return resInt
    
    
# Incorrect: Use hashmap to insert and get directly 
# Need to check parent path and current path
class FileSystem1:
    def __init__(self):
        print("Code1 - Incorrect")
        self.pathMap = {}
    def createPath(self, path: str, value: int) -> bool:
        if path in self.pathMap:
            return False
        self.pathMap[path] = value
        return True
    def get(self, path: str) -> int:
        if path in self.pathMap:
            return self.pathMap[path]
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)