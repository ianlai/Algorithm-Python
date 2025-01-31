# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/02/08 
    # Recursion [O(n): 49%]
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.tiltSum = 0 
        self.helper(root)
        return self.tiltSum
    
    def helper(self, root: Optional[TreeNode]) -> int:
        sumL = sumR = 0
        if root.left:
            _, sumL = self.helper(root.left)
        if root.right:
            _, sumR = self.helper(root.right)
        root.val = abs(sumL - sumR), sumL + sumR + root.val
        self.tiltSum += abs(sumL - sumR)
        return root.val 