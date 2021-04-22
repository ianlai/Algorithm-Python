# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS (53%)
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        deq = deque([root])
        ans = []
        
        while deq:
            ans.append([])
            for i in range(len(deq)):
                cur = deq.popleft()
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
                ans[-1].append(cur.val)
        
        return ans[::-1]