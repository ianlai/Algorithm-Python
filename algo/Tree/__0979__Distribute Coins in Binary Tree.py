# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n): 94%]
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.steps = 0
        def helper(root):
            if root is None:
                return 
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