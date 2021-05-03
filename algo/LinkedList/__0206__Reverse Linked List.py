# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:      
    
    # Iterative [O(n), 61%]
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        #dummy = ListNode(0)
        #dummy.head = head
        p1 = None #Not need dummy node
        p2 = head
        p3 = head.next
        print(p2.val)
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3          
            if p3:
                p3 = p3.next
        #dummy = None
        return p1
            