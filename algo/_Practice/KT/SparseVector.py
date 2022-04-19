
from xml.dom import IndexSizeErr
class Node:
    def __init__(self, idx = None, val = None):
        self.idx = idx
        self.val = val
        self.next = None 

class SparseVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node()
        #self.size = 0

    def set(self, idx, val):
        if idx >= self.capacity:
            raise IndexSizeErr
        cur = self.head
        while cur.next: 
            if cur.next.idx == idx:
                cur.next.val = val
                return 
            elif cur.next.idx < idx:
                cur = cur.next
            else:
                curNextKeep = cur.next
                cur.next = Node(idx, val)
                cur.next.next = curNextKeep
                return 
        cur.next = Node(idx, val)
        return 

    def get(self, idx):
        if idx >= self.capacity:
            raise IndexSizeErr
        cur = self.head
        while cur.next:
            if cur.next.idx == idx:
                return cur.next.val
            elif cur.next.idx < idx:
                cur = cur.next
            else:
                return 0
        return 0
    
    def toString(self):
        cur = self.head
        res = []
        for i in range(self.capacity):
            if cur.next is None:
                break
            if i < cur.next.idx:
                res.append(0)
            elif i == cur.next.idx:
                res.append(cur.next.val)
                cur = cur.next
        res.extend([0] * (self.capacity - len(res)))
        return res

    def __str__(self):
        res = ""
        cur = self.head
        while cur.next: 
            res += "[" + str(cur.next.idx) + "," + str(cur.next.val) + "] ->"
            cur = cur.next
        return res

if __name__ == '__main__':
    print("SparseVector")
    v1 = SparseVector(10)
    v1.set(0, 5)
    v1.set(8, 13)
    v1.set(3, 6)
    print(v1.get(4))
    print(v1.get(8))
    print(v1.get(3))
    print(v1.get(9))
    #print(v1.get(10))
    print(v1)
    print(v1.toString())
    v1.set(10, 15)
