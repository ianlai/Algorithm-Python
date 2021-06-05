DEBUG = False

# Data strcture design 
# Hashmap : find O(1) + LinkedList : move to tail and pop head O(1)  [16%]

class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
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