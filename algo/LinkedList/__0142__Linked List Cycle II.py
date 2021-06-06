# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return None
        
        p1, p2 = head, head.next
        
        while True:

            if p1 == p2:
                break 
            
            if not p1 or not p2 or not p2.next:
                return None
            
            p1 = p1.next
            p2 = p2.next.next 
        
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1