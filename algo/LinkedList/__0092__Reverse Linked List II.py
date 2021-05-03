# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # Iterative [O(n), 56%]
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return head 
        
        dummy = ListNode(0)
        dummy.next = head
        p0 = head
        count = 0
        p1 = dummy 
        
        while p0:
            p0 = p0.next 
            count += 1
        print("count:", count)
        
        # Special cases
        if count == 1:
            return head
        if left == count:
            return head
           
        # Preparation
        for i in range(left-1):
            p1 = p1.next
        
        if p1.next:
            p2 = p1.next 
        if p2.next:
            p3 = p2.next
        beforeTarget = p1
        afterTarget = p2
        
        # Revert
        for i in range(right - left + 1):
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next
                
        # Connect the 3 segments 
        beforeTarget.next = p1
        afterTarget.next = p2
        
        # Choose the node to return for different 4 cases
        if left == 1 and right == count:  #e.g. [1, 5]
            return p1
        if left == 1:                     #e.g. [1, 3]
            return beforeTarget.next
        if right == count:                #e.g. [3, 5]
            return head
        return head                       #e.g. [2, 4]
        
            
            