# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n), 97%]
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res
        
    def dfs(self, node, res):
        if not node:
            return -1
        left = self.dfs(node.left, res)
        right = self.dfs(node.right, res)
        layer = max(left, right) + 1 
        while len(res) <= layer:
            res.append([])
        res[layer].append(node.val)
        return layer