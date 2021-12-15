# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Count the nodes [O(n): 98%]
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        count = 1
        p1 = head 
        while p1.next:
            p1 = p1.next
            count += 1
        k %= count
        if k == 0:
            return head
        tail = p1 
        
        
        p1 = head
        for _ in range(count - k - 1):
            p1 = p1.next
        newHead = p1.next 
        p1.next = None
        tail.next = head
        return newHead 