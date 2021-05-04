# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    
    # BFS [O(n), 79%]
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        print("BFS")
        if not root:
            return []
        
        deq = deque([root])
        ans = []
        
        while deq:
            ans.append([])
            for i in range(len(deq)):
                cur = deq.popleft()
                ans[-1].append(cur.val)
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
        return ans
    
    # ===============================================
    
    # DFS [?, 6%] 
    # Search with DFS by "layer times" 
    # The targetLevel increments by 1 for each DFS 
    # Time = 1 + (1 + 2) + (1 + 2 + 4) + (1 + 2 + 4 + 8) 
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        print("DFS")
        if not root:
            return []
        
        targetLevel = 0
        ans = []
        while True:
            layer = []
            self.dfs(targetLevel, 0, layer, root)
            if layer:
                ans.append(layer)
            else:
                break 
            targetLevel += 1
        return ans
    
    def dfs(self, targetLevel, level, layer, node): 
        if not node:
            return 
        if level == targetLevel:
            layer.append(node.val)
            return 
        self.dfs(targetLevel, level + 1, layer, node.left)
        self.dfs(targetLevel, level + 1, layer, node.right)
                
            