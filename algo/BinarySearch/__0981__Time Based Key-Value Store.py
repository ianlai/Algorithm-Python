#2021/12/11
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        print("Code-2")
        self.tmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        arr = self.tmap[key]
        
        start, end = 0, len(arr) 
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid][0] < timestamp:
                start = mid + 1
            elif arr[mid][0] > timestamp:
                end = mid
            else:
                return arr[mid][1]
        return arr[start - 1][1] if start != 0 else ""
        
#========================================
#2021/11/01
class TimeMap1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        print("Code-1")
        self.tmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    # Binary Search [O(logn): 42%]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""
        arr = self.tmap[key]
        
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2 
            if timestamp == arr[mid][0]:
                return arr[mid][1]
            elif timestamp > arr[mid][0]:
                l = mid 
            else:
                r = mid
                
        if timestamp < arr[l][0]: 
            return ""
        elif timestamp == arr[l][0]: 
            return arr[l][1]
        elif timestamp >= arr[r][0]: 
            return arr[r][1]
        else:
            return arr[l][1]
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)