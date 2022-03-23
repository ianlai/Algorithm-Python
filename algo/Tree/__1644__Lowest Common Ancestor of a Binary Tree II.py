# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # LCA-2: return the number of found nodes [O(n): 93%] 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code2")
        def helper(root, p, q):
            if root is None:
                return None, 0
            
            if root == p or root == q:
                _, cl = helper(root.left, p, q)
                _, cr = helper(root.right, p, q)
                if cl == 1 or cr == 1:
                    return root, 2
                else:
                    return root, 1
        
            left, countl = helper(root.left, p, q)
            right, countr = helper(root.right, p, q)

            if left and right:
                return root, 2
            if left:
                if countl == 2:
                    return left, 2
                return left, 1
            if right:
                if countr == 2:
                    return right, 2
                return right, 1
            return None, 0
        
        lca, count = helper(root, p, q)
        return lca if count == 2 else None
    
    # ==============================
    # LCA-1 [Incorrect for LCA-2]
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code1")
        if root == p or root == q:
            return root
        
        if root is None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None