class ULLNode:
    def __init__(self, val = 0):
        self.arr = [val]
        self.next = None

class UnrolledLinkedList():
    def __init__(self, capacity):
        print("UnrolledLinkedList is created. Capacity = ", capacity)
        self.capacity = capacity 
        self.preHead = ULLNode()
        
    def append(self, val):
        pre = self.preHead
        cur = pre.next
        if cur:
            while cur:
                cur = cur.next
                pre = pre.next
        else:
            pre.next = ULLNode(val)
            cur = pre.next
            
        if len(pre.arr) < self.capacity:
            pre.arr.append(val)
        else:
            pre.next = ULLNode(val)
        
    def get(self, idx):
        cur = self.preHead.next
        if not cur:
            return -1
        while cur:
            if idx >= len(cur.arr):
                idx -= len(cur.arr)
                cur = cur.next
            else:
                return cur.arr[idx]
        return -1
    
    def insert(self, idx, val): 
        #print("insert", val, "at", idx)
        pre = self.preHead
        cur = pre.next
        if not cur:
            if idx == 0:
                cur = ULLNode(val)
                pre.next = cur
            else:
                print("Insert idx is invalid")
                return -1
        
        while cur:
            if idx >= len(cur.arr):
                #print("jump")
                idx -= len(cur.arr)
                cur = cur.next
                pre = pre.next
            else:
                #size < capacity
                if len(cur.arr) < self.capacity:
                    #print("insert")
                    cur.arr.insert(idx, val)
                #size >= capacity 
                else:
                    #print("new node")
                    cur.arr.insert(idx, val)
                    nextHead = cur.next
                    cur.next = ULLNode(cur.arr[-1])
                    cur.arr.pop() 
                    cur.next.next = nextHead
                break
        return -1
    
    def printList(self):
        pre = self.preHead
        cur = pre.next
        while cur:
            print(cur.arr, "->", end = "")
            cur = cur.next
        print()
    
    def printArray(self):
        arr = []
        pre = self.preHead
        cur = pre.next
        while cur:
            arr.extend(cur.arr)
            cur = cur.next
        print(arr)

    def getArray(self):
        arr = []
        pre = self.preHead
        cur = pre.next
        while cur:
            arr.extend(cur.arr)
            cur = cur.next
        return arr

if __name__ == "__main__":
    print("Main of UnrolledLinkedList")
    ull = UnrolledLinkedList(3)
    ull.append(10)
    ull.append(11)
    ull.append(12)
    ull.append(13)
    ull.append(14)
    ull.append(15)

    ull.insert(3,3)
    ull.insert(5,5)
    ull.insert(3,33)
    ull.printArray()
    ull.printList()

