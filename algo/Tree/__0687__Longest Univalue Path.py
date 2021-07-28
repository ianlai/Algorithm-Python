# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: 
            return 0
        consecutiveCur, longestCur = self.findLongest(root)
        
        return max(consecutiveCur, longestCur)

    def findLongest(self, root):
        if not root:
            return 0, 0
        consecutiveL, longestL = self.findLongest(root.left)
        consecutiveR, longestR = self.findLongest(root.right)

        longestCur = max(longestL, longestR)

        consecutiveCur = 0
        
        if root.left and root.right and root.left.val == root.val == root.right.val:
            longestCur = max(longestCur, consecutiveL + consecutiveR + 2)
            consecutiveCur = max(consecutiveL, consecutiveR) + 1
        else:
            if root.left and root.left.val == root.val:
                consecutiveCur = consecutiveL + 1
            if root.right and root.right.val == root.val:
                consecutiveCur = max(consecutiveR + 1, consecutiveL)

        longestCur = max(longestCur, consecutiveCur)
        return consecutiveCur, longestCur