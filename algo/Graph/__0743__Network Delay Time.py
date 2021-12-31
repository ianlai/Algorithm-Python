class Solution:
    
    # 2021/12/31 
    # Bellmon-Ford [O(EV): 7% -> 29%(with optimization)]
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        print("Code4: Bellmon-Ford")
        
        distance = [inf] * (n + 1)
        distance[k] = 0 
        
        for _ in range(n-1):   #relax V-1 times 
            isChanged = False
            for u, v, w in times:
                if distance[u] + w < distance[v]:
                    isChanged = True
                    distance[v] = distance[u] + w
            if not isChanged:  #optimization (if no change then break)  
                break
        
        maxTime = max(distance[1:])
        return maxTime if maxTime != inf else -1
    
    # =========================================================
    # 2021/12/31 
    # Dijkstra [O(ElogV): 27%]
    def networkDelayTime3(self, times: List[List[int]], n: int, k: int) -> int:
        print("Code3: Dijkstra")
        
        #Parse to prepare cost matrix 
        cost = collections.defaultdict(dict)  #c[u, v]
        for u, v, w in times:
            cost[u][v] = w
        
        #Dijkstra to updat distance array
        distance = [inf] * (n + 1)
        distance[k] = 0
        heap = [(0, k)]
        while heap:
            _, u = heapq.heappop(heap)
            for v, w in cost[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    heapq.heappush(heap, (distance[v], v))
                    
        if any(time == inf for time in distance[1:]):
            return -1
        else:
            return max(distance[1:])
        
    # =========================================================

    # 2021/06/20 
    # SSSP (Bellman-Ford) [O(EV):11% / O(V):96%]
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        print("Code2: Bellmon-Ford")
        if not times:
            return 0
        distance = [float('inf')] * n
        distance[k-1] = 0
        
        # Relax |V| - 1 times
        for _ in range(n-1):
            for u, v, w in times:
                if distance[u-1] + w < distance[v-1]:
                    distance[v-1] = distance[u-1] + w 
        print(distance)
        maxDistance = max(distance)
        return maxDistance if maxDistance != float('inf') else -1
        
    # =========================================================
    
    # 2021/06/20 
    # SSSP, using Dijkstra [O(ElogV):69% / O(E+V):87% ]
    # 說明：
    # Dijkstra -> O(ElogV) 
    # BFS      -> O(E + V)
    # 兩者幾乎是一樣的架構，但為什麼Dijkstra會花比較多的時間。
    # BFS是使用Deque，從左耗費O(1)取出頭，並且每一個元素都只會被放入deque一次。
    # Dijkstra則是使用heap，取出最小值需要花費O(logV)，
    # 且relaxation是可以讓一個node被更新好幾次的（所以沒有一個visited存在）
    # 因此Dijkstra的停止條件不是所有元素放入heap一遍，而是所有的d已經被更新好，使得沒有任何 d[v] > d[u] + c[u,v]  
    def networkDelayTime1(self, times: List[List[int]], n: int, k: int) -> int:
        print("Code1: Dijkstra")
        if not times:
            return 0
        
        distance = [float('inf')] * n               #d[u], d[v]
        distance[k - 1] = 0
        
        #parse
        nodeToTime = collections.defaultdict(dict)  #cost[u, v]
        for u, v, w in times:
            nodeToTime[u][v] = w
        
        #Dijkstra 
        heap = [[0, k]] #src
        while heap:
            curTime, curNode = heapq.heappop(heap)
            #print(curNode)
            for node, time in nodeToTime[curNode].items(): #curNode -> node takes time
                newTime = curTime + time
                if distance[node - 1] <= newTime: 
                    continue
                distance[node - 1] = newTime   #relaxation 
                heapq.heappush(heap, (newTime, node))
            
        #print(pathTimes)
            
        maxTime = max(distance)
        return maxTime if maxTime != float('inf') else -1