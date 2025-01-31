# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Iteration [O(M+N), 41%]
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3 = ListNode(0)  #new list       
        p1, p2, p3 = l1, l2, l3
        
        while p1 or p2:
            if not p1:
                p3.next = p2
                break
            if not p2:
                p3.next = p1
                break
            if p1.val >= p2.val:
                p3.next = p2
                p2 = p2.next
            else:
                p3.next = p1
                p1 = p1.next
            p3 = p3.next
        return l3.next