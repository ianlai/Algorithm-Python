# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # 2022/05/02 
    # LinkedList [O(n):43% / O(1):76%]
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while cur.next != None:
            p1 = cur.next
            skip = False
            while p1.next and p1.val == p1.next.val:
                p1 = p1.next
                skip = True
            if skip:
                cur.next = p1.next
                continue
            cur = cur.next
        
        return dummy.next 