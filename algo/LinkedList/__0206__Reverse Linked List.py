# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:      
    
    # 3 pointers, dummy node [O(n), 99%]
    # Note: remember to set head.next to None, otherwise it will be a circle
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        preHead = ListNode()
        preHead.next = head
        p1, p2, p3 = preHead, head, head.next
        
        while p2:
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next                
        head.next = None #<----FORGET
        return p1


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
            