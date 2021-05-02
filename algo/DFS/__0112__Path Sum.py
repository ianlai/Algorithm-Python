# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n), 79%] 
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, targetSum - root.val) 
            
    def helper(self, root, targetSum):
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            return False
        
        if root.left and self.helper(root.left, targetSum - root.left.val):
            return True
        if root.right and self.helper(root.right, targetSum - root.right.val):
            return True
        return False