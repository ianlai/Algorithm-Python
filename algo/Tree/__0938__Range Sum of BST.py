# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Recursion [O(n): 88%]
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0 
        
        rangeSum = 0
        if low <= root.val <= high:
            rangeSum += root.val
            rangeSum += self.rangeSumBST(root.left, low, high)
            rangeSum += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            rangeSum += self.rangeSumBST(root.left, low, high)
        else:
            rangeSum += self.rangeSumBST(root.right, low, high)
        return rangeSum
            
        