class Solution:
    
    # Binary Search [O(logn + klogk), 35%]
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        
        start, end = 0, len(arr) - 1
        ans = []
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if arr[mid] < x:
                start = mid
            elif arr[mid] > x:
                end = mid
            elif arr[mid] == x:
                start = end = mid 
                break 
        #print("start, end = ", start, end)
                
        for _ in range(k):
            element, start, end = self.getNext(arr, x, start, end)
            ans.append(element)
        #print(ans)
        return sorted(ans)
    
    
    def getNext(self, arr, x, start, end):
        if start < 0:
            return arr[end], start, end + 1
        if end >= len(arr):
            return arr[start], start - 1, end
        if start == end:
            return arr[start], start - 1, end + 1
        if abs(arr[start] - x) <=  abs(arr[end] - x):  #if distances of left and right are same, go with left 
            return arr[start], start - 1, end
        else:
            return arr[end], start, end + 1
            
            