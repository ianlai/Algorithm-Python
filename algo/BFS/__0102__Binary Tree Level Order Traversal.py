# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# BFS (79%)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
                
            