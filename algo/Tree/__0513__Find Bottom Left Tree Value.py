# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        deque = collections.deque([root])
        ans = 0
        while deque:
            for i in range(len(deque)):
                cur = deque.popleft()
                if i == 0:
                    ans = cur.val
                    
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
        return ans