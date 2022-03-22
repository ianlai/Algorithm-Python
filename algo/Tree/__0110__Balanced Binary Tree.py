# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/03/22 
    # Bottom-up [O(n): 85%]
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node is None:
                return 0, True
            l, bl = helper(node.left)
            r, br = helper(node.right)
            if abs(l - r) > 1 or not bl or not br:
                return 1 + max(l, r), False
            else:
                return 1 + max(l, r), True
        _, isbalanced = helper(root)
        return isbalanced