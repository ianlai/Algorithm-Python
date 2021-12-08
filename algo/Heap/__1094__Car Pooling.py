#https://leetcode.com/problems/car-pooling/
class Solution:
    
    # Heap [O(N+NlogN):44%]
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        fromMap = collections.defaultdict(list)
        for num, f, t in trips:
            fromMap[f].append([t, num])

        used, maxUsed = 0, 0 
        ends = []
        for f in sorted(fromMap.keys()):
            while ends:
                earlistEnd = ends[0]
                if earlistEnd[0] <= f:
                    heapq.heappop(ends)
                    used -= earlistEnd[1]
                else:
                    break
            for t, num in fromMap[f]:
                used += num 
                maxUsed = max(used, maxUsed)
                heapq.heappush(ends, [t, num])

        if maxUsed > capacity:
            return False
        return True