# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class Node:
    def __init__(self, nlist):
        self.arr = []        
        for ni in nlist:
            if ni.isInteger():
                self.arr.append(ni.getInteger())
            else:
                self.arr.append(Node(ni.getList()))
        
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.root = Node(nestedList)
        self.res = []
        self.dfs(self.root, self.res)
        self.idx = 0
        
    def dfs(self, root, res):
        if not root.arr:
            return 
        for a in root.arr:
            if isinstance(a, int):
                res.append(a)
            else:
                self.dfs(a, res)
        
    def next(self) -> int:
        ans = self.res[self.idx]
        self.idx += 1
        return ans
    
    def hasNext(self) -> bool:
        if self.idx == len(self.res):
            return False
        return True
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())