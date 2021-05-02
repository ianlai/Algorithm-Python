# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #DFS [O(n), 72%]
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.dfs(root, targetSum - root.val, ans, [root.val])
        return ans
    
    def dfs(self, root, targetSum, ans, cur):
        if not root.left and not root.right:
            if targetSum == 0:
                ans.append(cur)
            return 
        if root.left:
            lVal = root.left.val
            self.dfs(root.left, targetSum - lVal, ans, cur + [lVal])
        if root.right:
            rVal = root.right.val
            self.dfs(root.right, targetSum - rVal, ans, cur + [rVal])
        return 