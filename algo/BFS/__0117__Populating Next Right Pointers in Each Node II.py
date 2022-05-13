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
    
    #BFS [O(N): 86% / O(N): 48%]
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        deq = collections.deque([(root, 0)])
        prev = [None, 0] 
        while deq:
            cur = deq.popleft()
            if prev[0] is not None and prev[1] == cur[1]:
                prev[0].next = cur[0]
            if prev[1] < cur[1]:
                prev[0].next = None
            prev = cur
            
            if cur[0].left:
                deq.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                deq.append((cur[0].right, cur[1] + 1))
            
        return root

        
                
        