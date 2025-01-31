"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        
        deq = collections.deque([root])
        while deq:
            for i in range(len(deq)):
                cur = deq.popleft()
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
                if i > 0:
                    pre.next = cur
                pre = cur
            cur.next = None
        return root
            