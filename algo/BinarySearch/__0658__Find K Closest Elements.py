class Solution:

    # 2021/12/15 
    # Binary Search [O(logn + k): 41%]
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        print("Code3")
        start, end = 0, len(arr)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                start = mid
                break
            elif arr[mid] < x:
                start = mid + 1 
            else:
                end = mid
                
        res = []
        left, right = start - 1, start 
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
        return sorted(res)
        
    # ==========================================
    
    # 2021/07/03 
    # Binary Search [O(logn + k): 57%]
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        print("Code2")
        if not arr:
            return []
        
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]: 
            return arr[len(arr) - k :]
        
        idx = self.getClosestIdx(arr, x)
            
        print("closed idx:", idx, arr[idx])
        
        deq = collections.deque([arr[idx]])
        left, right = idx - 1, idx + 1
        for i in range(k-1):
            if left < 0:
                for j in range(k-1-i):
                    deq.append(arr[right])
                    right += 1
                break
            if right > len(arr) - 1:
                for j in range(k-1-i):
                    deq.appendleft(arr[left])
                    left -= 1
                break
                
            if abs(arr[left] - x) <= abs(arr[right] - x): # "=" is must
                #print("left", arr[left])
                deq.appendleft(arr[left])
                left -= 1
            else:
                #print("right", arr[right])
                deq.append(arr[right])
                right += 1
        return deq
    
    def getClosestIdx(self, arr, x):
        start, end = 0, len(arr) - 1
        idx = -1
        while start + 1 < end:
            mid = start + (end - start) // 2
            #print(start, mid, end)
            diff = arr[mid] - x
            if diff > 0:
                end = mid
            elif diff < 0:
                start = mid
            else:
                idx = mid
                break #mid
                
        if idx == -1:
            if abs(arr[start] - x) <= abs(arr[end] - x): # "=" is must
                idx = start
            else:
                idx = end
        return idx

    # ==========================================
    # Binary Search [O(logn + klogk), 35%]
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        print("Code1")
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