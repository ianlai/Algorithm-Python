class Solution:
    
    # 2022/05/21
    # Tarjans Algorithm [O(V+E): 43% / O(V+E): 90%]
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for v1, v2 in connections:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        def dfs(graph, res, lowestOrder, visited, preNode, curNode, curOrder):
            visited[curNode] = True
            lowestOrder[curNode] = curOrder
            #print(preNode, curNode, lowestOrder)
            for nextNode in graph[curNode]:
                if nextNode == preNode:
                    continue
                if not visited[nextNode]:
                    dfs(graph, res, lowestOrder, visited, curNode, nextNode, curOrder + 1)
                lowestOrder[curNode] = min(lowestOrder[curNode], lowestOrder[nextNode])
                if lowestOrder[nextNode] == curOrder + 1:
                    res.append([curNode, nextNode])
            #print("  ", preNode, curNode, lowestOrder)
        
        lowestOrder = [-1] * n
        visited = [False] * n
    
        res = []
        dfs(graph, res, lowestOrder, visited, -1, 0, 0)
        #print(lowestOrder)
        
        return res