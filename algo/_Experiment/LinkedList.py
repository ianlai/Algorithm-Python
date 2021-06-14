class LLNode:
    def __init__(self, val = -1):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.preHead = LLNode()
        self.tail = self.preHead

    def get(self, idx):
        cur = self.preHead.next
        while cur and idx > 0:
            cur = cur.next
            idx -= 1
        return cur.val if cur else None

    def append(self, val):
        self.tail.next = LLNode(val)
        self.tail = self.tail.next

    def insert(self, idx, val):
        pre = self.preHead
        cur = self.preHead.next
        while cur and idx > 0:
            cur = cur.next
            pre = pre.next
            idx -= 1

        if not cur:
            if idx == 0:
                self.append(val)
                return 1
            else:
                print("Invalid index")
                return -1
        
        pre.next = LLNode(val)
        pre.next.next = cur
        return 1

    def printList(self):
        cur = self.preHead.next
        while cur:
            print(cur.val, "-> ", end = "")
            cur = cur.next
        print()
    
    def printArray(self):
        arr = []
        cur = self.preHead.next
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)

    def getArray(self):
        arr = []
        cur = self.preHead.next
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr


# ll = LinkedList()


# for i in range(10):
#     ll.append(i)
# ll.printList()
# print(ll.get(2))
# print(ll.get(15))
# print(ll.get(9))
# print(ll.get(10))
# print(ll.get(11))

# ll.insert(3,33)
# ll.insert(0,100)
# ll.insert(15,150)
# ll.insert(12,120)
# ll.printList()
# ll.printArray()