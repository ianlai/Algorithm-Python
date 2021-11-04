# Store changing history and do binary search to get [37%]
class SnapshotArray:

    def __init__(self, length: int):
        #self.arr = [0] * length        #not need to store the array 
        
        #self.history = [[]] * length   #can't declare two dimension array like this since all sub-array will be changed together
        self.history = [[[0, 0]] for _ in range(length)]
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        #print("set:", index, "->", val, self.history)
        self.history[index].append([self.snapId, val])

    def snap(self) -> int:
        #print("snap:", self.history)
        oldId = self.snapId
        self.snapId += 1 
        return oldId

    def get(self, index: int, snap_id: int) -> int:
        #print("get:", index, snap_id, self.history)
        
        #Binary search to find snap_id in history[index]
        start, end = 0, len(self.history[index])
        if start == end:
            return 0
        
        while start < end:
            mid = start + (end - start) // 2
            if self.history[index][mid][0] == snap_id:
                #return self.history[index][mid][1]
                start = mid + 1 
            elif self.history[index][mid][0] < snap_id:  
                start = mid + 1 
            else:
                end = mid 
            
        if self.history[index][mid][0] <= snap_id:
            return self.history[index][mid][1] 
        return self.history[index][mid-1][1]
    
# =============================================
# Store all history [TLE]
class SnapshotArray1:

    def __init__(self, length: int):
        self.arr = [[0] * length]

    def set(self, index: int, val: int) -> None:
        self.arr[-1][index] = val

    def snap(self) -> int:
        self.arr.append(list(self.arr[-1]))
        return len(self.arr) - 2

    def get(self, index: int, snap_id: int) -> int:
        return self.arr[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)