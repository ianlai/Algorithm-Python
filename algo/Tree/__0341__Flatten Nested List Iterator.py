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


# Use recursive to store the flattern result in an array
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = self.initialize(nestedList)
        self.idx = 0
    
    def initialize(self, nlist):
        arr = []        
        for e in nlist:
            if e.isInteger():
                arr.append(e.getInteger())  #append
            else:
                arr.extend(self.initialize(e.getList()))  #extend
        return arr
        
    def next(self) -> int:
        res = self.arr[self.idx]
        self.idx += 1
        return res
    
    def hasNext(self) -> bool:
        if self.idx == len(self.arr):
            return False
        return True
    

# Form a tree, run DFS in init to store the flattern result in a res arr
# 轉換成樹多此一舉

# class Node:
#     def __init__(self, nlist):
#         self.arr = []        
#         for e in nlist:
#             if e.isInteger():
#                 self.arr.append(e.getInteger())
#             else:
#                 self.arr.append(Node(e.getList()))
        
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         self.root = Node(nestedList)
#         self.res = []
#         self.idx = 0
        
#         self.dfs(self.root)
        
#     def dfs(self, root):
#         if not root.arr:
#             return 
#         for e in root.arr:
#             if isinstance(e, int):
#                 self.res.append(e)
#             else:
#                 self.dfs(e)
        
#     def next(self) -> int:
#         ans = self.res[self.idx]
#         self.idx += 1
#         return ans
    
#     def hasNext(self) -> bool:
#         if self.idx == len(self.res):
#             return False
#         return True
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())