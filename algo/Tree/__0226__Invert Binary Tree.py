# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 1-step swap (python)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    # 3-step swap
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root