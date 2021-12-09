#https://leetcode.com/problems/car-pooling/
class Solution:
    
    # 2021/12/09
    # Store all timestamps and pop from heap [O(N+NlogN):87%]
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        print("Code-2: Store all timestamps and pop from heap")
        timestamps = []
        for trip in trips:
            heappush(timestamps, (trip[1], trip[0]))
            heappush(timestamps, (trip[2], -trip[0]))
        used = 0
        while timestamps:
            t = heappop(timestamps)
            used += t[1]
            if used > capacity:
                return False
        return True
    
    # ===============================================
    
    # 2021/12/08
    # Sort by from time, pop end time from heap [O(N+NlogN): 87%]
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        print("Code-1: Sort by from time, pop end time from heap")
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
                if maxUsed > capacity:
                    return False
                heapq.heappush(ends, [t, num])
        return True