# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS + Sorted array [Time O(n) : 96% / Space O(n) : 94%]
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        sorted = []
        self.dfs(root, sorted)
        swap = []
        for i in range(1, len(sorted)):
            if sorted[i-1].val > sorted[i].val:
                if len(swap) == 0:
                    swap.extend([sorted[i-1], sorted[i]])  #1,3,2,4  (special case)
                elif len(swap) > 0:
                    swap.append(sorted[i])  # 1,7,3,4,5,6,2,8 
        
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val
    
    def dfs(self, root, sorted):
        if not root:
            return
        self.dfs(root.left, sorted)
        sorted.append(root)
        self.dfs(root.right, sorted)
        
        
        
    
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         self.incorrectNodes = []
#         dummy = TreeNode(-float('inf'))
#         dummy.right = root
#         self.dfs(dummy, dummy.right)
#         print(self.incorrectNodes)
        
    
#     def dfs(self, parent, root):
#         if not root:
#             return
        
#         while  
        
#         last = self.dfs(root.left)
#         if last.val > root.val:
#             self.incorrectNodes.append(last)
#         self.dfs(root.right)
#         return 