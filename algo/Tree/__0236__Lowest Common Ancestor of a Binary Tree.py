# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Test case:
    # [37,-34,-48,null,-100,-101,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
    # 48
    # -71
    
    # 2022/03/15
    # Recursion [O(n): 71%]
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code2")
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left  = self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None: #has values for both
            return root
        if left:
            return left
        if right: 
            return right
        
    # ==========================================   
    # 2021/05/15
    # Recursion [O(n), 62%]
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("Code1")
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        leftResponse  = self.lowestCommonAncestor(root.left, p, q)
        rightResponse = self.lowestCommonAncestor(root.right, p, q)
        
        if not leftResponse and not rightResponse:
            return None
        if leftResponse and rightResponse:
            return root
        if leftResponse:
            #return root.left   #left next 
            return leftResponse #left answer
        if rightResponse:
            #return root.right
            return rightResponse