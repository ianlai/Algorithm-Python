# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        sumArr = [0]
        self.helper(root, sumArr)
        return root
    
    def helper(self, root, sumArr):
        if root is None:
            return
        
        self.helper(root.right, sumArr)
        sumArr[0] += root.val
        root.val = sumArr[0]
        self.helper(root.left, sumArr)
        return sumArr[0]