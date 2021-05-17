# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Divide and Conquer [O(n), 92%]
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.flattenGetLast(root)
        return root
    
    # Purpose 1: Flattern (so both left and right need to call this)
    # Purpose 2: Return Last 
    def flattenGetLast(self, root):
        if not root:
            return None
        leftLast  = self.flattenGetLast(root.left)
        rightLast = self.flattenGetLast(root.right)
        
        if leftLast:
            leftLast.right = root.right
            root.right = root.left
            root.left = None 
        if rightLast:
            return rightLast
        if leftLast:
            return leftLast
        return root
        
        
      #### Bad (mix recursion and iteration)
    
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return None
#         #print(root.val)
        
#         cur = root
#         while cur.right:
#             self.helper(cur)
#             cur = cur.right
#         return root
    
#     def helper(self, root):
#         if not root:
#             return 
#         print(root.val)
#         if root.left:
#             rightLast = self.helper(root.left)
#             rightLast.right = root.right
#             root.right = root.left
#             root.left = None 
        
#         while root.right:
#             root = root.right