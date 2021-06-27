# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        p1, p2 = head, head.next
        while p2:
            if p1.val == p2.val:
                p2 = p2.next
                p1.next = p2
            else:
                p1 = p1.next
                p2 = p2.next
        return head