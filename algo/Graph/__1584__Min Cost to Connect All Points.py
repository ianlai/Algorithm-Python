class Solution:
    
    # 2022/04/26 
    # Minimum Spanning Tree (Prim) [O(n2logn): 5% / O(n2): 91%]
    #
    # 距離都當場算，其實可以先算好。
    # 兩個for迴圈是相同邏輯，可以統一。
    # visited的部分做了兩次判斷，有點亂，要再整理
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0
            
        start = points[0]
        heap = []
        for i in range(1, len(points)):
            dist = abs(points[i][0] - start[0]) + abs(points[i][1] - start[1]) 
            heapq.heappush(heap, (dist, start, points[i]))
        

        visited = set()
        visited.add(tuple(start))
        totalDistance = 0
        while heap:
            d, p1, p2 = heapq.heappop(heap)
            if tuple(p2) in visited:
                continue
            totalDistance += d
            visited.add(tuple(p2))
            for i in range(len(points)):
                if points[i] == p2 or tuple(points[i]) in visited:
                    continue
                dist = abs(points[i][0] - p2[0]) + abs(points[i][1] - p2[1]) 
                heapq.heappush(heap, (dist, p2, points[i]))

        return totalDistance 