# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    # 2022/04/22
    # DFS [O(H): 71%]
    # 一路往下找最大值，跟最大值比，比較大就加一
    
    # 使用nested function + nonlocal var 
    def goodNodes(self, root: TreeNode) -> int:
        print("Code2")
        if not root:
            return 0
        
        def helper(root, maxVal): 
            nonlocal counter
            if not root:
                return 
            if root.val >= maxVal:
                counter += 1
            maxVal = max(root.val, maxVal)
            helper(root.left, maxVal)
            helper(root.right, maxVal)
        
        counter = 0
        helper(root, -float('INF'))
        return counter
    
    # =======================================
    
    # DFS
    # 使用class variable 
    def goodNodes1(self, root: TreeNode) -> int:
        print("Code1")
        if not root:
            return 0
        
        self.counter = 0
        self.helper(root, -float('INF'))
        return self.counter
    
    def helper(self, root, maxVal): 
        if not root:
            return 
        if root.val >= maxVal:
            self.counter += 1
        maxVal = max(root.val, maxVal)
        self.helper(root.left, maxVal)
        self.helper(root.right, maxVal)