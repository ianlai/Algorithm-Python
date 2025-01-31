# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
DEBUG = False

class Solution:
    
    # Space requirement is O(1) => array is not allowed
    # (1) Find the list of right half (including middle if num of node is odd), cut the list into 2 halves
    # (2) Reverse the left half 
    # (3) Traverse the left list and right list to compare 
    # [time: O(n) 93%, space: O(1) 95%]
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:      #0
            return True
        if not head.next: #1
            return True
        
        headRight, isOdd = self.divideAndfindRightIsOdd(head)
        headLeft       = self.reverse(head)
        print("IsOdd:", isOdd)
        print("Left head:", headLeft.val)
        print("Right head:", headRight.val)
        
        #Compare left list and right list 
        p1, p2 = headLeft, headRight
        if isOdd:
            p2 = p2.next
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
            
    def divideAndfindRightIsOdd(self, head):
        dummy = ListNode()
        dummy.next = head
        p1, p2, p3 = dummy, head, head
        isOdd = True
        while True:
            if not p3:
                isOdd = False
                break
            if not p3.next:
                isOdd = True
                break
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next.next
        headRight = p2 
        self.printList("Right:", headRight)
        p1.next = None    #divide left and right
        return headRight, isOdd
    
    def reverse(self, head):
        p1, p2, p3 = None, head, head.next 
        while p2:
            p2.next = p1 
            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next
        headLeft = p1
        self.printList("Left: ", headLeft)
        return headLeft
    
    def printList(self, msg, head):
        if not DEBUG:
            return 
        cur = head
        print(msg)
        while cur != None:
            print(str(cur.val) + "->", end = "")
            cur = cur.next
        print()