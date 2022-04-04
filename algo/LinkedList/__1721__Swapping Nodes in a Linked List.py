# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    #Linkedlist, swap value (not node) [O(n): 21%]
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 0:
            return head
        
        def findNode(head, k):
            dummy = ListNode(0)
            dummy.next = head
            cur = dummy 
            for i in range(k):
                cur = cur.next
            return cur
        
        node = head
        n = 0
        while node is not None:
            node = node.next 
            n += 1
        
        node1 = findNode(head, k)
        node2 = findNode(head, n - k + 1)

        node1.val, node2.val = node2.val, node1.val
        return head
    
        