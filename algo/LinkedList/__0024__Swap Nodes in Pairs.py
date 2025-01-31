# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 2021/12/29 
    # O(n)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head 
        p1, p2, p3 = dummy, head, head.next
        newHead = p3
        while p2:
            if p2.next is None:
                break
            p2 = p2.next.next
            p3.next = p1.next
            p1.next.next = p2
            p1.next = p3 
            p1 = p1.next.next
            if p2:
                p3 = p2.next
        return newHead