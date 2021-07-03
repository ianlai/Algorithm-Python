# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: #0
            return head 
        if not head.next: #1
            return head
        
        leftList, rightList = self.separateList(head)        
        leftList = self.sortList(leftList)
        rightList = self.sortList(rightList)
        sortedList = self.mergeList(leftList, rightList)

        return sortedList
    
    def separateList(self, head):        
        p1, p2 = head, head
        p0 = ListNode(0)  #dummy 
        p0.next = p1
        while p2 and p2.next:
            p0 = p0.next
            p1 = p1.next
            p2 = p2.next.next
        p0.next = None
        return head, p1
    
    def mergeList(self, left, right):
        p0 = ListNode(0)
        dummy = p0
        while left and right:
            if left.val <= right.val:
                p0.next = left
                left = left.next
                p0 = p0.next
            else:
                p0.next = right
                right = right.next
                p0 = p0.next
        if left:
            p0.next = left
        else:
            p0.next = right
        return dummy.next
            
    def printList(self, head):
        p1 = head
        while p1: 
            print(p1.val, "->", end = "")
            p1 = p1.next
        print()
            