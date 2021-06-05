import heapq
class Solution:
    
    # max-heap [O(k + (n-k)logk), 77%]
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("max-heap")
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
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        print("min-heap")
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
        
        
        