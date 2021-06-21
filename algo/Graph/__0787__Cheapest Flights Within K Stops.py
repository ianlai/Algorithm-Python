class Solution:
    # Tese case:
    # 5
    # [[0,1,100],[1,2,100],[0,2,500],[2,3,200],[2,4,400],[3,4,100]]
    # 0
    # 4
    # 2
    
    # Tese case:
    # 11
    # [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
    # 0
    # 2
    # 4
    
    #====================================
    
    # Top-Down DP [O(V^2*K) 20%]
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print("Top-Down DP")
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

    # Dijkstra's variant [O(ElogV), 80%]
    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        print("Dijkstra")
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
                # else:
                #     print("case3 skip: ", node)
            
        print(distanceList)
        print(stopList)
            
        maxTime = max(distanceList)
        return maxTime if maxTime != float('inf') else -1