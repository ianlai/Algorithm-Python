class Solution:
    # Test case:
    # 5
    # [[0,1,100],[1,2,100],[0,2,500],[2,3,300],[2,4,600],[3,4,100]]
    # 0
    # 4
    # 2
    
    # Test case:
    # 11
    # [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    # 0
    # 2
    # 4
    
    # Test case:
#     17
# [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
# 13
# 4
# 13
    
    #====================================
    
    # 2021/12/31
    # Dijkstra's variant []
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print("Code3: Dijkstra")
        if not flights:
            return 0
        
        print("src->dst: ", src, "->", dst, " k=", k)
        distanceList = [inf] * n
        distanceList[src] = 0
        stopList = [inf] * n
        stopList[src] = 0
        
        #Parse and generate cost matrix
        cost = collections.defaultdict(dict)
        for u, v, w in flights:
            cost[u][v] = w
        
        #Dijkstra varient to update distance array 
        #Regular Dijkstra: insert the new node v that matches d[u] + cost[u, v] < d[v]
        #Varient Dijkstra: insert the new node v that matches 
        #                  (1) d[u] + cost[u, v] < d[v] or 
        #                  (2) stop[u] + 1 < stop[v]
        heap = [(0, -1, src)] #src (time, stop, node)
        while heap:
            curTime, curStop, curNode = heapq.heappop(heap)
            #print("out: [node, time, stop]" , curNode, curTime, curStop)
            if curStop > k:
                continue
            if curTime < distanceList[curNode]:  
                distanceList[curNode] = curTime  #update distanceList when pulling out
                stopList[curNode] = curStop      #update stopList when pulling 
                
            if curNode == dst: #exit (MUST, wrong if without this)
                return curTime
            
            for nextNode, nextTime in cost[curNode].items(): #curNode -> node takes time
                if curTime + nextTime < distanceList[nextNode] or curStop + 1 < stopList[nextNode]:
                #print("   in: [node, time, stop]", node, curTime + time, curStop + 1)
                    heapq.heappush(heap, (curTime + nextTime, curStop + 1, nextNode))
            
        #print("distanceList:", distanceList)
        #print("stopList:", stopList)
            
        return distanceList[dst] if distanceList[dst] != inf else -1
    
    #====================================
    
    # Top-Down DP [O(V^2*K) 20%]
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print("Code2: Top-Down DP")
        if not flights:
            return 0
        cityToPrice = collections.defaultdict(dict)
        for u, v, w in flights:
            cityToPrice[u][v] = w
        memo = {}
        minCost = self._findCheapestPrice(cityToPrice, src, k, dst, memo) #DP
        return minCost if minCost != float('inf') else -1
        
    # cur, k are variable
    def _findCheapestPrice(self, mp, cur, k, dst, memo):
        if cur == dst:
            return 0
        if k < 0 :
            return float('inf') 
        if (cur, k) in memo:
            return memo[(cur, k)]
        
        minCost = float('inf')
        for nextNode, nextCost in mp[cur].items():
            minCost = min(minCost, nextCost + self._findCheapestPrice(mp, nextNode, k-1, dst, memo))
        memo[(cur, k)] = minCost
        return minCost
        
    #====================================

    # 2021/06/21
    # Dijkstra's variant [O(ElogV), 80%]
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print("Code1: Dijkstra")
        if not flights:
            return 0
        
        print("src", src, "dst", dst)
        distanceList = [float('inf')] * n  #O(V)
        distanceList[src] = 0
        stopList = [float('inf')] * n      #O(V)
        stopList[src] = 0
        
        #parse
        nodeToTime = collections.defaultdict(dict) #O(V2)
        for u, v, w in flights:
            nodeToTime[u][v] = w
        print(nodeToTime)
        
        #Dijkstra 
        heap = [(0, 0, src)] #src (time, stop, node)
        while heap:
            curTime, curStop, curNode = heapq.heappop(heap)
            print("Node, time, stop:" , curNode, curTime, curStop)
            
            if curNode == dst: #exit (MUST, wrong if without this)
                print("distanceList:", distanceList)
                print("stopList:", stopList)
                return curTime
            if curStop > k:
                continue
            
            for node, time in nodeToTime[curNode].items(): #curNode -> node takes time
                #print("next node", node, time)
                newTime = curTime + time
                #print("time: ", distanceList[node], newTime)
                
                # case1: 新的cost 比 現存的 到node的path distance 還小
                # case2: 新的stop數 比 現存的 到node的stop數還小 （還有機會）
                # 不論是哪個，都會加入heap來考慮
                # 雖然distanceList和stopList都只能存一個值，但如果找到dst就會跳出去，所以舊的資料用不到可以蓋掉
                # add a new node with updated values rather than 
                # updating the value of the existing node.
                if newTime < distanceList[node] or curStop < stopList[node]:
                    #print("case1:", distanceList, stopList)
                    distanceList[node] = newTime   #relaxation 
                    stopList[node] = curStop
                    heapq.heappush(heap, (newTime, curStop + 1, node))
            
        print("distanceList:", distanceList)
        print("stopList:", stopList)
            
        maxTime = max(distanceList)
        return maxTime if maxTime != float('inf') else -1