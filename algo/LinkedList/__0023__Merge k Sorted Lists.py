# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    
    #WIP 
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        res = ListNode(0)
        p1 = res
        
        hq = []
        for head in lists:
            heapq.heappush(hq, [head.val, head])   #val, node
        
        numOfEnded = 0
        while numOfEnded < len(lists): 
            _, node = heapq.heappop(hq)
            p1.next = node
            p1 = p1.next
            if node.next:
                node = node.next
                heapq.heappush(hq, [node.val, node])
            else:
                numOfEnded += 1
        return res.next
            
    # ================================================
            
    # Merge lists one by one [O(kN): 7%]
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        print("Merge lists one by one")
        if not lists:
            return None
        
        result = lists[0]
        for i in range(1, len(lists)):
            result = self.merge(result, lists[i])
        return result
    
    def merge(self, list1, list2):
        p1 = list1
        p2 = list2 
        res = ListNode(0)
        p3 = res
        while p1 and p2: 
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        return res.next