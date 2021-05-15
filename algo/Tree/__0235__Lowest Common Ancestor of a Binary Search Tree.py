# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # [O(n), 44%]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        a, b = 0, 0
        if p.val > q.val:
            a, b = q.val, p.val
        else:
            a, b = p.val, q.val
            
        if a <= root.val <= b:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        if left:
            return left
        
        right = self.lowestCommonAncestor(root.right, p, q)
        if right:
            return right