# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:             #MUST to have to end the recursion
            return TreeNode(head.val) #TreeNode
        
        mid = self.getMidNode(head)
        #print("Mid:", mid)
        #self.printList(head)
        #self.printList(mid.next)
        
        midTreeNode = TreeNode(mid.val)
        midTreeNode.left = self.sortedListToBST(head)
        midTreeNode.right = self.sortedListToBST(mid.next)
        
        return midTreeNode
    
    def getMidNode(self, head):
        p0 = ListNode(0)
        p0.next = head
        p1, p2 = head, head
        while p2 and p2.next:
            p0 = p0.next
            p1 = p1.next
            p2 = p2.next.next
        p0.next = None #Two heads: head, p1 
        return p1
    
    def printList(self, head):
        p1 = head
        while p1:
            print(p1.val, "->", end = "")
            p1 = p1.next
        print()