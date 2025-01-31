class Node:
    def __init__(self, idx = -1, val = -1):
        self.idx = idx
        self.val = val
        self.next = None

# 2022/06/13 
# LinkedList [O(N): 71% / O(N): 27%]
class SparseVector:
    def __init__(self, nums: List[int]):
        self.prehead = Node()
        cur = self.prehead
        for i, v in enumerate(nums):
            if v == 0:
                continue
            cur.next = Node(i, v)
            cur = cur.next
        self.print()
        
    def print(self):
        cur = self.prehead
        while cur:
            cur = cur.next

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1 = self.prehead.next
        p2 = vec.prehead.next
        product = 0
        while p1 and p2:
            if p1.idx == p2.idx:
                product += p1.val * p2.val
                p1 = p1.next
                p2 = p2.next
            elif p1.idx < p2.idx:
                p1 = p1.next
            else:
                p2 = p2.next
        return product
            
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)