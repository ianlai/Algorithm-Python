"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    
    # LCA3 - Find root first then LCA1 [O(n): 43%]
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root = p 
        while root.parent:
            root = root.parent
            
        def findLCA(root, p, q):
            if root is None:
                return None
            if root == p or root == q:
                return root
            
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        
        return findLCA(root, p, q)