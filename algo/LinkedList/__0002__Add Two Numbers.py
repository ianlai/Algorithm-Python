# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def printList(self, msg, head):
        print(msg, end = "")
        p1 = head
        while p1:
            print(str(p1.val) + "->", end = "")
            p1 = p1.next
        print()
        
        
    # [O(M+N), 88%]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        # self.printList("L1: ", l1)
        # self.printList("L2: ", l2)
        # #l1 = self.reverse(l1)
        # #l2 = self.reverse(l2)
        # self.printList("L1: ", l1)
        # self.printList("L2: ", l2)
        p1, p2 = l1, l2
        
        dummy = ListNode()
        p3 = dummy
        
        carry = 0
        while p1 and p2:
            val = p1.val + p2.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry = 1
            p3.next = ListNode(val)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        
        while p1:
            val = p1.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry = 1
            p3.next = ListNode(val)
            p1 = p1.next
            p3 = p3.next
        
        while p2:
            val = p2.val + carry
            carry = 0
            if val > 9:
                val -= 10
                carry = 1
            p3.next = ListNode(val)
            p2 = p2.next
            p3 = p3.next
        
        if carry == 1:
            p3.next = ListNode(1)
        
        # self.printList("L3: ", dummy.next)
        # l3 = dummy.next 
        # l3Last = self.reverse(dummy)
        # l3.next = None
        return dummy.next
    
    def reverse(self, head):
        if not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        p1, p2, p3 = dummy, head, head.next
        while p2:
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next
        head.next = None #FORGOT
        return p1
        
        
        
        
        