# Store changing history and do binary search to get [37%]
class SnapshotArray:

    def __init__(self, length: int):
        print("Version-3")
        self.history = [[[0, 0]] for _ in range(length)] #add the version version when initialized 
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        if self.snapId == self.history[index][-1][0]:
            self.history[index][-1] = [self.snapId, val]
        else:
            self.history[index].append([self.snapId, val])

    def snap(self) -> int:
        oldId = self.snapId
        self.snapId += 1  
        return oldId

    #Binary search to find snap_id in history[index]
    def get(self, index: int, snap_id: int) -> int:
        arr = self.history[index]
        start, end = 0, len(arr)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid][0] == snap_id:
                return arr[mid][1]  #return directly since no duplicated id in Version3
                #start = mid + 1 
            elif arr[mid][0] < snap_id:  
                start = mid + 1 
            else:
                end = mid 
        return arr[start-1][1] 
    
# =============================================

# Store changing history and do binary search to get [37%]
class SnapshotArray2:

    def __init__(self, length: int):
        #self.arr = [0] * length       #not need to store the array 
        #self.history = [[]] * length  #can't declare 2D array like this since all sub-array will be changed together
        print("Version-2")
        self.history = [[[0, 0]] for _ in range(length)] #add the version version when initialized 
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snapId, val])

    def snap(self) -> int:
        oldId = self.snapId
        self.snapId += 1  
        return oldId

    #Binary search to find snap_id in history[index]
    def get(self, index: int, snap_id: int) -> int:
    
        start, end = 0, len(self.history[index])
        while start < end:
            mid = start + (end - start) // 2
            if self.history[index][mid][0] == snap_id:
                #return self.history[index][mid][1]    #not found yet, need to find the last one, not arbitrary one
                start = mid + 1 
            elif self.history[index][mid][0] < snap_id:  
                start = mid + 1 
            else:
                end = mid 
        return self.history[index][start-1][1] 
    
# =============================================
   
# Store changing history and do binary search to get [37%]
class SnapshotArray1:

    def __init__(self, length: int):
        #self.arr = [0] * length       #not need to store the array 
        #self.history = [[]] * length  #can't declare 2D array like this since all sub-array will be changed together
        print("Version-1")
        self.history = [[[0, 0]] for _ in range(length)] #add the version version when initialized 
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        self.history[index].append([self.snapId, val])

    def snap(self) -> int:
        oldId = self.snapId
        self.snapId += 1  
        return oldId

    #Binary search to find snap_id in history[index]
    def get(self, index: int, snap_id: int) -> int:
    
        start, end = 0, len(self.history[index])
        if start == end:
            return 0
        
        while start < end:
            mid = start + (end - start) // 2
            if self.history[index][mid][0] == snap_id:
                #return self.history[index][mid][1]    #not found yet, need to find the last one, not arbitrary one
                start = mid + 1 
            elif self.history[index][mid][0] < snap_id:  
                start = mid + 1 
            else:
                end = mid 
            
        if self.history[index][mid][0] <= snap_id:
            return self.history[index][mid][1] 
        return self.history[index][mid-1][1]