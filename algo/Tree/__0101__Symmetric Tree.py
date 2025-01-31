# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        return self.isTwoTreeSymmetric(root.left, root.right)
    
    def isTwoTreeSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left:
            return False
        if not right:
            return False
        
        if left.val != right.val:
            return False
        if not self.isTwoTreeSymmetric(left.left, right.right): #outer
            return False
        if not self.isTwoTreeSymmetric(left.right, right.left): #inner
            return False
        
        return True
        