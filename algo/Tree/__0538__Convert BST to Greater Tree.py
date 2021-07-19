# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        self.helper1(root)
        self.helper2(root, 0)
        return root
        
    def helper1(self, root):
        if not root:
            return 0
        r = self.helper1(root.right)
        root.val += r 
        l = self.helper1(root.left)
        return root.val + l
    
    def helper2(self, root, parentVal):
        if not root:
            return 
        root.val += parentVal 
        self.helper2(root.left, root.val)
        self.helper2(root.right, parentVal)
        return 
        