import random

'''
2022/05/28 
直接把數值用list和set兩種方法存，但這樣的刪除其實是O(N)，不符合規定的。 
[TC: 47% / SC: 6%]
'''
class RandomizedSet:
    
    def __init__(self):
        print("Code2")
        self.set = set()
        self.arr = []
    
    # O(1)
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False 
        self.set.add(val)
        self.arr.append(val)
        return True
    
    # O(N) 
    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False 
        
        self.arr.remove(val)
        self.set.remove(val)
        return True
    
    # O(1)
    def getRandom(self) -> int:
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]

'''
2021/07/19 
利用把要刪除的元素搬到最後，把size指標往內移一格代表刪除(soft delete) 
[TC: 42% / SC: 89%]
'''
class RandomizedSet:

    # Use set to support O(1) insert and remove
    # Use list to support O(1) getRandom [36%]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        print("Code1")
        self.mp = dict() #key -> idx
        self.ar = [] 
        self.size = 0    #必要的，因為arr內不一定都是valid，有些後面的部分已經soft刪掉了
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        
        #加入的時候也要分成arr已經完全沒有空間，需要append，或是可以使用之前soft delete刪除騰出來的空間兩種case
        self.mp[val] = self.size  #index
        if self.size >= len(self.ar):
            self.ar.append(val)
        else:
            self.ar[self.size] = val
            
        self.size += 1
        return True

    # 刪掉的動作通常都要O(N)，為了要達到O(1)刪除，我們必須採用soft delete
    # 所以把要被刪掉的元素搬到最後，把size pointer往內縮一格，這樣那個刪除元素就用不到了（雖然實際上還留著）
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