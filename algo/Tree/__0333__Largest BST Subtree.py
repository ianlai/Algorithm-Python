# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2021/12/27
    # Recursion, return 4 parameters: in, contain, max, min [O(n): 72%]
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxInRoot, maxContainsRoot, _, _ = self._largestBSTSubtree(root)
        return max(maxInRoot, maxContainsRoot)
    
    def _largestBSTSubtree(self, root: Optional[TreeNode]) -> int:   
        if root.left is None and root.right is None:
            return 1, 1, root.val, root.val
        
        maxContainsRoot = 0
        maxLeft, maxRight, minLeft, minRight = -inf, -inf, inf, inf
        maxInLeft, maxInRight = 0, 0
        maxContainsLeft, maxContainsRight = 0, 0
        isBST = True
        
        if root.left:
            maxInLeft, maxContainsLeft, maxLeft, minLeft = self._largestBSTSubtree(root.left)
            if maxLeft >= root.val or maxContainsLeft == 0:
                isBST = False
        if root.right:
            maxInRight, maxContainsRight, maxRight, minRight = self._largestBSTSubtree(root.right)
            if root.val >= minRight or maxContainsRight == 0:
                isBST = False
        if isBST:
            maxContainsRoot = maxContainsLeft + maxContainsRight + 1
            
        maxInRootmax, maxContainsRoot, maxRoot, minRoot = (
            max(maxContainsRoot, maxInLeft, maxInRight), 
            maxContainsRoot, 
            max(maxLeft, root.val, maxRight), 
            min(minLeft, root.val, minRight))
        
        #print(root.val, "->", maxInRootmax, maxContainsRoot, maxRoot, minRoot)
        return maxInRootmax, maxContainsRoot, maxRoot, minRoot
    