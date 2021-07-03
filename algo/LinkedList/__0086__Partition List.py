# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        
        l1 = ListNode(0)
        l2 = ListNode(0)
        p1, p2 = l1, l2
        p0 = head 
        
        while p0:
            if p0.val < x:
                p1.next = p0
                p0 = p0.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = p0
                p0 = p0.next
                p2 = p2.next
                p2.next = None
        p1.next = l2.next
        return l1.next