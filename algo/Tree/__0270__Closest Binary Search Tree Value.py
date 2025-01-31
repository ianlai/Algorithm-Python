# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:           
    # Recursion (not traversal) + Global variable [O(n), 64%]
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return -1
        self.minDistance = abs(root.val - target)
        self.minDistanceNode = root
        
        self.helper(root, target)
        return self.minDistanceNode.val
        
    def helper(self, root, target):
        if not root:
            return 
        print(root.val, self.minDistanceNode.val)
        
        if abs(root.val - target) < self.minDistance: 
            self.minDistance = abs(root.val - target)
            self.minDistanceNode = root
        
        if target > root.val:
            self.helper(root.right, target)
        elif target < root.val:
            self.helper(root.left, target)