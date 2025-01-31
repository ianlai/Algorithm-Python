# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/05/08 
    # DFS-Post [O(n): 80%]
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        print("Code4")
        step = 0
        
        # diff: num of coin - num of coin
        def dfs(root):
            nonlocal step
            if not root:
                return 0
            diffL = dfs(root.left)
            diffR = dfs(root.right)      
            diffRoot = root.val + diffL + diffR - 1 #root.val (coin) - 1 (node)
            step += abs(diffL) + abs(diffR)
            return diffRoot
        
        dfs(root)
        return step
    
    # 2021/10/09 
    # DFS [O(n): 80%]
    def distributeCoins3(self, root: Optional[TreeNode]) -> int:
        print("Code3")
        
        def helper(root):
            if not root:
                return 0, 0
            diffL, stepL = helper(root.left)        #coin - node (left)
            diffR, stepR = helper(root.right)       #coin - node (right)
            diffRoot = root.val + diffL + diffR - 1 #coin - node (root)
            stepRoot = abs(diffL) + abs(diffR) + stepL + stepR
            return diffRoot, stepRoot
        
        _, stepRoot = helper(root)
        return stepRoot
    
    #====================================================

    # DFS [O(n): 80%]
    def distributeCoins2(self, root: Optional[TreeNode]) -> int:
        print("Method2")
        self.steps = 0
        def helper(root):
            if not root:
                return 0
            
            diffL, diffR = 0, 0
            if root.left:
                diffL = helper(root.left)  #coin - node (left)
            if root.right:
                diffR = helper(root.right) #coin - node (right)
                
            diffRoot = root.val + diffL + diffR - 1 #coin - node (root )
            self.steps += abs(diffL) + abs(diffR)
            
            return diffRoot
        helper(root)
        return self.steps
        
    #====================================================
            
    # DFS [O(n): 94%]
    def distributeCoins1(self, root: Optional[TreeNode]) -> int:
        print("Method1")
        self.steps = 0
        def helper(root):
            if root is None:
                return 0, 0, 0, 0
            nodeL, coinL, nodeR, coinR = 0, 0, 0, 0
            if root.left:
                nodeLL, coinLL, nodeLR, coinLR = helper(root.left)
                nodeL = nodeLL + nodeLR + 1
                coinL = coinLL + coinLR + root.left.val
                
            if root.right:
                nodeRL, coinRL, nodeRR, coinRR = helper(root.right)
                nodeR = nodeRR + nodeRL + 1
                coinR = coinRL + coinRR + root.right.val
                
            self.steps += abs(nodeL - coinL) + abs(nodeR - coinR)
            return nodeL, coinL, nodeR, coinR
            
        helper(root)
        return self.steps    