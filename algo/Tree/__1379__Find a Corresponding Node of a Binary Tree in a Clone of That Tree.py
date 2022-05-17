# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 2022/05/17
    # DFS [O(N): 67% / O(1): 40%]
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def findNode(cloned, targetVal):
            if cloned is None:
                return None
            
            if cloned.val == targetVal:
                return cloned
            
            left = findNode(cloned.left, targetVal)
            if left is not None:
                return left
                
            right = findNode(cloned.right, targetVal)
            if right is not None:
                return right
            
        return findNode(cloned, target.val)