# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/05/03
    # DFS [TC: O(2n): 68% / SC: O(h): 9%]
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            curSum = dfs(node.left) + dfs(node.right) + node.val
            return curSum
        
        def dfsTarget(node, target):
            if not node:
                return False, 0
            
            left = dfsTarget(node.left, target) 
            if left[0]:
                return True, 0
            
            right = dfsTarget(node.right, target) 
            if right[0]:
                return True, 0
            
            curSum = left[1] + right[1] + node.val
            if curSum == target and node != root:
                return True, curSum
            else:
                return False, curSum
        
        total = dfs(root)
        if total % 2 == 1:
            return False
        isValid, _ = dfsTarget(root, total//2)
        return isValid