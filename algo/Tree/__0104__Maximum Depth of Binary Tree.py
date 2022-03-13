# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/03/13
    # Recursion [O(n): 94%]
    def maxDepth(self, root: TreeNode) -> int:
        print("Code2")
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        
    # =========================================
            
    #2021/07/01
    def maxDepth1(self, root: TreeNode) -> int:
        print("Code1")
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        return max(left, right) + 1 