"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    # [39%]
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        p1 = head
        preHead2 = Node(0)
        p2 = preHead2
        oldToNew = {}
        
        while p1:
            p2.next = Node(p1.val)
            oldToNew[p1] = p2.next
            p1 = p1.next
            p2 = p2.next
    
        p1 = head
        p2 = preHead2.next
        while p1:
            if p1.random:
                p2.random = oldToNew[p1.random]
            p1 = p1.next
            p2 = p2.next
        
        return preHead2.next
            
        
        