# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Node:
    def __init__(self, val, node):
        self.val = val
        self.node = node
        
    def __lt__(self, other):
        if self.val <= other.val:
            return True
        return False
    
class Solution:
    
    #Priority Queue + Implement a wrapper [O(nlogk): 41%]
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        print("Priority Queue")
        if not lists:
            return None
        
        res = ListNode(0)
        p1 = res
        hq = []
        numOfEnded = 0
        
        for head in lists:
            if not head:
                numOfEnded +=1 
                continue
            
            #heapq.heappush(hq, [head.val, head])   #array: val, node
            n = Node(head.val, head)                #wrap in a node class
            heapq.heappush(hq, n)   #val, node
                
        while numOfEnded < len(lists): 
            n = heapq.heappop(hq)
            node = n.node
            p1.next = node
            p1 = p1.next
            if node.next:
                node = node.next
                n = Node(node.val, node)
                heapq.heappush(hq, n)
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