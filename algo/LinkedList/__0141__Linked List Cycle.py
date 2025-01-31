# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return False
        
        p1, p2 = head, head.next
        
        while True:

            if p1 == p2:
                return True
            
            if not p1 or not p2 or not p2.next:
                return False
            
            p1 = p1.next
            p2 = p2.next.next 