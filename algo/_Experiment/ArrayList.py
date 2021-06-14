class ArrayList:
    def __init__(self):
        self.arr = []

    def get(self, idx):
        if idx < len(self.arr):
            return self.arr[idx]
        return None

    def append(self, val):
        self.arr.append(val)

    def insert(self, idx, val):
        if idx < len(self.arr):
            self.arr.insert(idx, val)
            return 1 
        print("Invalid index") 
        return -1

    def printArray(self):
        print(self.arr)

    def getArray(self):
        return self.arr