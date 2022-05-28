import random
class RandomizedSet:

    # Use set to support O(1) insert and remove
    # Use list to support O(1) getRandom [36%]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = dict()
        self.ar = []
        self.size = 0
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        
        self.mp[val] = self.size  #index
        if self.size >= len(self.ar):
            self.ar.append(val)
        else:
            self.ar[self.size] = val
            
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.mp:
            return False
        
        idx = self.mp[val]
        del self.mp[val]
        
        if self.size - 1 != idx:
            self.ar[idx] = self.ar[self.size - 1]
            self.mp[self.ar[idx]] = idx
    
        self.size -= 1
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand = random.randint(0, self.size - 1)
        return self.ar[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()