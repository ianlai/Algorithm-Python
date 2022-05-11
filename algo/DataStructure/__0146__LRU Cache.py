DEBUG = False


# 2022/05/11
'''
Map                [get: O(1) / set: O(1)]
Double Linked List [move to head: O(1) / pop tail: O(1)]
=> Using Double Linked List is easier to implement 
'''
class DLN:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 
        
class LRUCache:
    def __init__(self, capacity):
        print("Code2")
        self.head = DLN()
        self.tail = DLN()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.keyToNode = {}
        self.cap = capacity
    
    def get(self, key):
        kToN = self.keyToNode
        if key in kToN:
            node = kToN[key]
            self.moveToHead(node)
            return node.val
        return -1
            
    def put(self, key, val):
        kToN = self.keyToNode
        if key in kToN:
            node = kToN[key]
            node.val = val #set
            self.moveToHead(node)
        else:
            self.addHead(key, val)
            
            #Evict 
            if len(kToN) > self.cap:
                self.popTail()
            
    def addHead(self, key, val):
        newNode = DLN(key, val)
        self.keyToNode[key] = newNode    #add key
        self._addNode(newNode)           #add node
        
    def moveToHead(self, node):
        self._removeNode(node)  #removeNode和addNode順序不能反過來
        self._addNode(node)
        
    def popTail(self):
        prevKey = self.tail.prev.key     
        del self.keyToNode[prevKey]      #remove key
        prev = self.tail.prev
        self._removeNode(prev)           #remove node
    
    '''
    Add node between head and first element (or tail)
    '''
    def _addNode(self, node):
        old = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = old
        old.prev = node
    '''
    Remove any node
    '''
    def _removeNode(self, node):
        prev = node.prev
        after = node.next
        
        prev.next = after
        after.prev = prev
        
    def _print(self):
        cur = self.head
        while cur:
            print(cur.key, "->", end = "")
            cur = cur.next
        print()

        
        
#============================================================
        
# 2021/06/05

# Data strcture design 
# Hashmap : find O(1) + Single LinkedList : move to tail and pop head O(1)  [16%]
class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        
class LRUCache1:

    def __init__(self, capacity: int):
        print("Code1")
        self.dummy = Node()  #head = dummy.next
        self.keyToPrev = {}
        self.tail = self.dummy    #tail
        self.capacity = capacity

    def get(self, key: int) -> int:
        self.printDebug("========== GET:" + str(key))
        
        if key in self.keyToPrev:
            prev = self.keyToPrev[key]
            curVal = prev.next.val
            self.kick(prev)
            self.printDebugFull()
            return curVal
        else:
            self.printDebugFull()
            return -1
        
    def kick(self, prev):
        cur = prev.next 
        if cur == self.tail:                     #special case: only one node (except dummy)  <--FORGOT
            return 
        
        prev.next = cur.next                     #remove cur
        self.keyToPrev[cur.next.key] = prev      #update next's mapping  <--- FORGOT
        self.pushBack(cur)    #push cur to tail
        
    def pushBack(self, cur):
        cur.next = None                        
        self.keyToPrev[cur.key] = self.tail      #update cur's mapping <--- FORGOT
        self.tail.next = cur
        self.tail = cur
        
    # -------------------------
    
    def put(self, key: int, value: int) -> None:
        self.printDebug("========== PUT:" + str(key) + str(value))
        
        if key in self.keyToPrev:
            prev = self.keyToPrev[key]
            cur = prev.next
            cur.val = value                  #update cur's value
            self.kick(prev)
        else:
            newNode = Node(key, value)
            self.keyToPrev[key] = self.tail  #update prep's mapping to tail (cur will be a new tail)
            self.pushBack(newNode)           #new node so pushBack is enough, kick is not needed 
            
            if len(self.keyToPrev) > self.capacity:
                self.printDebug("!!! Evict")
                self.popFront()
                
        self.printDebugFull()
                
    def popFront(self):
        if self.dummy == self.tail:                 #special case: empty 
            return        
        head = self.dummy.next               
        del self.keyToPrev[head.key]                #remove head's key 
        self.dummy.next = head.next                 #remove head's node
        self.keyToPrev[head.next.key] = self.dummy  #update new head's mapping  <--- FORGOT
    
    # ===============================================
    
    def printList(self):
        cur = self.dummy 
        while cur != None:
            print((cur.key, cur.val), " -> ", end = "")
            cur = cur.next
        print()
    
    def printDebugFull(self):
        if not DEBUG:
            return
        
        print("Map size:", len(self.keyToPrev))
        for key in self.keyToPrev:
            if not self.keyToPrev[key]:
                continue
            print([key, self.keyToPrev[key].key, self.keyToPrev[key].val], end = "")
        print()
        self.printList()
        print("--------")
        
    def printDebug(self, msg):
        if not DEBUG:
            return 
        print(msg)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)