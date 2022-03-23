# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # 2022/03/24
    # Two pointer [Time O(M+N): 60% / Space O(1): 28%]
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        print("Code2")
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        return pA
        
        
    # 2021/07/01 
    # Two pointer [Time O(M+N): 47% / Space: O(1): 68%]
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        print("Code1")
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
        #print(p1.val, p1.next.val)
        #print(p2.val, p2.next.val)
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        # Recover the B linklist's structure
        tailB.next = None
        
        return p1
        
        