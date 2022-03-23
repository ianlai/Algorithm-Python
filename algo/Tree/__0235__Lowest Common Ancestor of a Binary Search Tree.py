# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 2022/03/23
    # BST LCA [O(n): 89%%]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code3")
        if not root:
            return None
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val :
            return root
        
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
    # 2022/03/23
    # Generalize LCA [O(n): 45%]
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code2")
        if root == p or root == q:
            return root
        if root is None:
            return None
        left  = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
    
    # 2021/05/15
    # BST LCA [O(n), 44%]
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code1")
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