class Solution:
    
    # Dijstra (DP, multiple condition) + prune: O(ElogV): 18% (TLE if no prune)
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for v1, v2, toll in highways:
            graph[v1][v2] = toll
            graph[v2][v1] = toll
        #distances = collections.defaultdict(int) #node, discounts -> distance
        distances = collections.defaultdict(lambda: collections.defaultdict(int)) 
        #print(graph)
        
        maxDiscounts = {} 
        
        res = inf
        heap = [(0, discounts, 0)]  #cost, discounts, node
        while heap:
            cost, discounts, cur = heapq.heappop(heap)
            if discounts < 0:
                continue
                
            # No prune
            # if cur in distances and discounts in distances[cur]:
            #     if cost < distances[cur][discounts]:
            #         distances[cur][discounts] = cost
            #     continue

            if cur in distances:
                if discounts <= maxDiscounts[cur]:
                    continue
                if cost < distances[cur][discounts]:
                    distances[cur][discounts] = cost
                
            distances[cur][discounts] = cost
            maxDiscounts[cur] = discounts
            if cur == n - 1 :
                res = min(res, cost)
            
            for nxt, cToN in graph[cur].items():
                heapq.heappush(heap, (distances[cur][discounts] + cToN, discounts, nxt))
                if discounts > 0:                    
                    heapq.heappush(heap, (distances[cur][discounts] + cToN // 2, discounts - 1, nxt))        

        return res if res != inf else -1