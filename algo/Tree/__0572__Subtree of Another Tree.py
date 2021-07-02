# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        return self.dfs(root, subRoot)
    
    def dfs(self, root, sub):
        if not root:
            return False 
        if sub.val == root.val and self.isSameTree(root, sub):    #match from this node
            return True
        if self.dfs(root.left, sub) or self.dfs(root.right, sub): #match from children's node
            return True
        return False
        
    def isSameTree(self, root, sub):
        if not root and not sub:
            return True
        if not root or not sub:
            return False
        if root.val != sub.val:
            return False
        return self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right)