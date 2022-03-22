import heapq
class Solution:
    
    # 2022/03/22
    # Quick select [O(nlogn) worst:O(n2) 52%] 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("Code3: Quickselect")
        distances = [(p1**2 + p2**2, (p1, p2)) for p1, p2 in points]
        def findTopK(arr, start, end, k):
            l, r = start, end
            mid = start + (end - start) // 2
            pivot = arr[mid][0]
            while l <= r:
                while l <= r and arr[l][0] < pivot:
                    l += 1
                while l <= r and arr[r][0] > pivot:
                    r -= 1
                if l <= r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
            if k <= r:
                return findTopK(arr, start, r, k)
            elif k >= l:
                return findTopK(arr, l, end, k)
            else:
                return arr[:k+1]
        closests = findTopK(distances, 0, len(distances)-1, k-1)
        res = [p[1] for p in closests]
        return res
                
    # ================================
    # 2021/06/05
    # max-heap [O(k + (n-k)logk), 77%]
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("Code2: max-heap")
        if not points or k == 0:
            return []
        
        distances = []
        for i in range(k):
            p = points[i]
            val = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(distances, (-val, p))
            
        for i in range(len(points)-k):
            i = i + k 
            p = points[i]
            val = p[0] * p[0] + p[1] * p[1]
            if -val > distances[0][0]:
                heapq.heappop(distances)
                heapq.heappush(distances, (-val, p))
        
        return [d[1] for d in distances]
    
    # ================================
    
    # min-heap [O(n + klogn), 76%]
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("Code1: min-heap")
        if not points or k == 0:
            return []
        
        distances = []
        for p in points:
            val = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(distances, (val, p))
            #distances.append((val, p))
        
        results = []
        for _ in range(k):
            results.append(heapq.heappop(distances)[1])
        return results
    
    # ================================
    
    # Built-in sorting [O(n2), 5%]
    def kClosest1(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("Built-in sorting")
        if not points or k == 0:
            return []
        
        distances = []
        for p in points:
            val = p[0] * p[0] + p[1] * p[1]
            distances.append((val, p))
        return [node[1] for node in sorted(distances)[:k]]
        
        
        