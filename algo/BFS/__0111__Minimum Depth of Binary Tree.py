# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# BFS (95%)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        deq = deque([root])
        level = 1
        
        while deq:
            for i in range(len(deq)):
                cur = deq.popleft()
                if not cur.left and not cur.right:
                    return level
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
                #value doesn't matter
            level += 1 
        return level

                
            