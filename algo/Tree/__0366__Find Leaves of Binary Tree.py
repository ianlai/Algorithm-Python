# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/25
    # Postorder DFS [Time: O(n + hlogh): 53% / Space: O(n + h): 27%]
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        print("Code2")
        
        def dfs(node, levelToNodes):
            if node is None:
                return 0
            
            left  = dfs(node.left, levelToNodes)
            right = dfs(node.right, levelToNodes)
            
            level = max(left, right) + 1
            levelToNodes[level].append(node.val)
            return level
        
        if not root:
            return []
        
        levelToNodes = collections.defaultdict(list)
        dfs(root, levelToNodes)
        
        res = []
        for key in sorted(levelToNodes.keys()):
            res.append(levelToNodes[key])
        return res
    
    # ==========================================================
    
    # 2021/07/01 
    # Postorder DFS (no sorting) [Time: O(n): 77% / Space: O(n + h): 76%]
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        print("Code1")
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