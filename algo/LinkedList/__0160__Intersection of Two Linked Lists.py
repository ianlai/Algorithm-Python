# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    #Two pointer [O(M+N), 30%]
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB 
        
        # Connect B's tail to B's head to form a cycle
        while curB.next:
            curB = curB.next
        tailB = curB
        curB.next = headB
        
        # Prepare for slow/faster pointers
        p1 = headA
        if not headA.next:
            tailB.next = None
            return None
        p2 = headA.next

        # Slow pointer and faster pointer meet
        while p1 != p2:
            if not p1 or not p2 or not p1.next or not p2.next:
                tailB.next = None
                return None
            p1 = p1.next
            p2 = p2.next.next
        
        # Find the meeting point 
        p1 = ListNode(0) 
        p1.next = headA
        print(p1.val, p1.next.val)
        print(p2.val, p2.next.val)
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        # Recover the B linklist's structure
        tailB.next = None
        
        return p1
        
        