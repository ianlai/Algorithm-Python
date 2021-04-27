# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        deq = deque([root])
        ans = []
        
        while deq:
            for i in range(len(deq)):
                cur = deq.popleft()
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
                #print(cur.val, " ", end = "")
            #print(" ")
            ans.append(cur.val)
        return ans
        