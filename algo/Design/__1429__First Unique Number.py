DEBUG = False


# Hashmap + LinkList [find: O(1) / add: O(1) --> 20%]  
class Node:
    def __init__(self, key = 0):
        self.key = key
        self.next = None
        
class FirstUnique:

    def __init__(self, nums: List[int]):
        print("Hashmap + LinkedList")
        self.keyToPrev = {}
        self.dummy = Node()
        self.tail = self.dummy
        self.used = set([])
        
        for num in nums:
            self.add(num)
            
    def printList(self):
        if not DEBUG:
            return 
        
        cur = self.dummy 
        while cur != None:
            print(str(cur.key) + "->", end = "")
            cur = cur.next
        print()
        
    def printDebug(self, msg):
        if not DEBUG:
            return 
        print(msg)
        
    # O(1)
    def showFirstUnique(self) -> int:        
        if self.dummy == self.tail:
            return -1
        return self.dummy.next.key

    # O(1)
    def add(self, key: int) -> None:
        self.printDebug("=== add:" + str(key))
        self.printList()
        if key in self.used:
            return 
        
        if key in self.keyToPrev:
            self.printDebug("found")
            prev = self.keyToPrev[key]
            cur = prev.next 
            del self.keyToPrev[cur.key]
            
            if self.dummy.next == self.tail:   #1 element
                self.printDebug("1 element")
                self.tail = self.dummy
                self.tail.next = None 
            else:                              #more elements
                self.printDebug("more elements")
                if cur == self.tail:
                    self.printDebug("remove last")
                    prev.next = None 
                    self.tail = prev
                else:
                    self.printDebug("remove other")
                    self.keyToPrev[cur.next.key] = prev
                    prev.next = cur.next
            self.used.add(key)
            
        else:
            self.printDebug("new")
            self.tail.next = Node(key)         #attach cur 
            self.keyToPrev[key] = self.tail    #update cur's mapping
            self.tail = self.tail.next         #update tail 
        
        
# ============================================

# Array implementation [find: O(2n) / add: O(1) --> TLE]  
class FirstUnique1:

    def __init__(self, nums: List[int]):
        print("Array")
        self.nums = nums

    # O(2n)
    def showFirstUnique(self) -> int:
        if not self.nums:
            return -1
        
        s = self.nums
        count = {}
        for i in range(len(s)):  #traversal-1
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        for i in range(len(s)):  #traversal-2
            if count[s[i]] == 1:
                return s[i]
        return -1

    # O(1)
    def add(self, value: int) -> None:
        self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)