# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/05/07
    # DFS-Post [O(2^h):13% / O(2^h):93%] 
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        print("Code2")
        def helper(root):
            if root is None:
                return set()
            
            if root.left is None and root.right is None:
                return set([root.val])
            
            lefts, rights = set(), set()
            if root.left:
                lefts = helper(root.left)
            if root.right:
                rights = helper(root.right)
            
            possibleSums = set()
            for v in lefts:
                possibleSums.add(v + root.val)
            for v in rights:
                possibleSums.add(v + root.val)
            return possibleSums
        
        possibleSums = helper(root)
        return targetSum in possibleSums 
    
    
    # 2021/05/13 
    # DFS-Pre [O(n):91%/ O(n):93%] 
    def hasPathSum1(self, root: TreeNode, targetSum: int) -> bool:
        print("Code1")
        if not root:
            return False
        return self.helper(root, targetSum - root.val) 
            
    def helper(self, root, targetSum):
        if not root.left and not root.right:
            if targetSum == 0:
                return True
            return False
        
        if root.left and self.helper(root.left, targetSum - root.left.val):
            return True
        if root.right and self.helper(root.right, targetSum - root.right.val):
            return True
        return False