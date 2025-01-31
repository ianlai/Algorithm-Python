
# 2022/03/01 
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        #self.arr = [[]] * self.size                #super slow (7%)
        self.arr = [[] for _ in range(self.size)]   #super fast (93%)
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        for pair in self.arr[idx]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.arr[idx].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        if len(self.arr[idx]) == 0:
            return -1
        else:
            for k, v in self.arr[idx]:
                if k == key:
                    return v
            return -1 
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
    
        idx = key % self.size
        for pair in self.arr[idx]:
            if pair[0] == key:
                self.arr[idx].remove(pair)
                return 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class MyHashMap1:

    # Array + Module 
    # size = 10     -> 20%
    # size = 1000   -> 69%
    # size = 100000 -> 15%
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.arr = [[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        for pair in self.arr[idx]:
            if pair[0] == key:
                pair[1] = value
                return 
        self.arr[idx].append([key, value]) #not found 

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        for pair in self.arr[idx]:
            if pair[0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        for pair in self.arr[idx]:
            if pair[0] == key:
                self.arr[idx].remove(pair)
                return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)