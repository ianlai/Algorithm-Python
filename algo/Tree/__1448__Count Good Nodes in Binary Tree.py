# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n): 8%]
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.counter = 0
        self.helper(root, -float('INF'))
        return self.counter
    
    def helper(self, root, maxVal): 
        if not root:
            return 
        if root.val >= maxVal:
            self.counter += 1
        maxVal = max(root.val, maxVal)
        self.helper(root.left, maxVal)
        self.helper(root.right, maxVal)