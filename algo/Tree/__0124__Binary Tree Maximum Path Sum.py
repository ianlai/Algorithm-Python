# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/29 
    # Postorder DFS [O(n): 92% / O(h): 64%]
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        totalMax = -inf
        def dfs(node):
            nonlocal totalMax
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curMax = node.val + max(left, right, 0)
            totalMax = max(totalMax, curMax, left + right + node.val)
            return curMax
        dfs(root)
        return totalMax