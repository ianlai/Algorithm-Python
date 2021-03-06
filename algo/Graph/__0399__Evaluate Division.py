class Solution(object):
    
    # 2022/04/03
    # 對所有連通塊做DFS一次，一維pathMap [O(E + (V+E) + Q): 68%] 
    def calcEquation(self, equations, values, queries):
        print("*** Code-6")
        # Create linkMap: node1 -> node2 -> link rate
        linkMap = collections.defaultdict(dict)
        for i in range(len(values)):
            v1, v2 = equations[i]
            linkMap[v1][v2] = values[i]
            linkMap[v2][v1] = 1 / values[i]
        
        def dfs(graph, cur, head, rate, nodeToRate, nodeToHead):
            if cur in nodeToHead:
                return
            nodeToRate[cur] = rate
            nodeToHead[cur] = head
            for nxt in graph[cur]:
                dfs(graph, nxt, head, rate * graph[cur][nxt], nodeToRate, nodeToHead)
            
        # Create nodeToRate: node -> path rate
        # Create nodeToHead: node -> head node
        nodeToRate = collections.defaultdict(int)
        nodeToHead = collections.defaultdict(int)
        for node in linkMap.keys():
            dfs(linkMap, node, node, 1, nodeToRate, nodeToHead)

        # Traverse queries
        res = []
        for v1, v2 in queries:
            if v1 not in nodeToHead or v2 not in nodeToHead:
                res.append(-1)
                continue
            if nodeToHead[v1] == nodeToHead[v2]:
                res.append(nodeToRate[v2] / nodeToRate[v1])
            else:
                res.append(-1)
        return res
    
    # =========================================
    # 2022/04/03
    # 對所有連通塊做DFS一次，二維pathMap二維 [O(E + (V+E) + Q): 49%] 
    def calcEquation5(self, equations, values, queries):
        print("Code-5")
        # Create linkMap: node1 -> node2 -> link rate
        linkMap = collections.defaultdict(dict)
        for i in range(len(values)):
            v1, v2 = equations[i]
            linkMap[v1][v2] = values[i]
            linkMap[v2][v1] = 1 / values[i]
        
        def dfs(graph, cur, start, rate, pathMap):
            if cur in pathMap:
                return
            pathMap[cur][start] = rate
            for nxt in graph[cur]:
                dfs(graph, nxt, start, rate * graph[cur][nxt], pathMap)
            
        # Create pathMap: node -> representative -> path rate
        pathMap = collections.defaultdict(dict)
        for node in linkMap.keys():
            dfs(linkMap, node, node, 1, pathMap)

        # Traverse queries
        res = []
        for v1, v2 in queries:
            if v1 not in pathMap or v2 not in pathMap:
                res.append(-1)
                continue
            if list(pathMap[v1].keys())[0] == list(pathMap[v2].keys())[0]:
                res.append(list(pathMap[v2].values())[0] / list(pathMap[v1].values())[0])
            else:
                res.append(-1)
        return res

    # =========================================
    
    # 2022/04/01
    # 對所有點做DFS一次 [O(E + VE + Q): 60%] 
    def calcEquation4(self, equations, values, queries):
        print("* Code-4")
        
        def dfs(start, cur, graph, pathMap):
            assert cur in pathMap[start]
            
            for next_node in graph[cur]:
                if next_node in pathMap[start]:
                    continue
                pathMap[start][next_node] = pathMap[start][cur] * graph[cur][next_node]
                dfs(start, next_node, graph, pathMap)
                
        #Generate the graph
        graph = collections.defaultdict(dict)
        for i in range(len(equations)):
            v1, v2 = equations[i]
            rate = values[i]
            graph[v1][v2] = rate
            graph[v2][v1] = 1/rate

        #Generate pathMap for all nodes  
        pathMap = collections.defaultdict(dict)
        for node in graph.keys():
            pathMap[node][node] = 1 
            dfs(node, node, graph, pathMap)

        #Generate the result array
        result = []
        for v1, v2 in queries:
            if v2 in pathMap[v1]:
                result.append(pathMap[v1][v2])
            else:
                result.append(-1)

        return result

    # =========================================
    
    # 2022/03/23
    # DFS [Time O(E + min(V, Q)*E] : 91% / Space O(E): 10%]
    # 只針對Query的點來跑DFS，且不重複跑
    # 缺點：還是遍歷很多次，且兩層defaultdict不必要
    def calcEquation3(self, equations, values, queries):
        print("Code-3")
        
        def generateLinkGraph(equations, values):
            graph = collections.defaultdict(lambda: collections.defaultdict(int)) #link
            for i in range(len(values)):
                n1, n2 = equations[i][0], equations[i][1]
                graph[n1][n2] = values[i]
                graph[n2][n1] = 1 / values[i]
            return graph
        
        def generatePathGraph(equations, graph):
            distance = collections.defaultdict(lambda: collections.defaultdict(int)) #path
            nodes = set()
            for n1, n2 in equations:
                nodes.add(n1)
                nodes.add(n2)
                
            def dfs(graph, distance, start, cur):
                for nxt in graph[cur]:
                    if nxt in distance[start]:
                        continue
                    if nxt in graph[start]:
                        distance[start][nxt] = graph[start][nxt]
                    else:
                        distance[start][nxt] = distance[start][cur] * graph[cur][nxt] 
                    dfs(graph, distance, start, nxt)

            for start in list(nodes):
                dfs(graph, distance, start, start)
            return distance
    
        graph = generateLinkGraph(equations, values)
        distance = generatePathGraph(equations, graph)
        
        # Debug 
        #print("Link:")
        #for k, v in graph.items():
        #    print(k, "->", v)
        #print("Path:")
        #for k, v in distance.items():
        #    print(k, "->", v)
            
        res = []
        for n1, n2 in queries:
            if distance[n1][n2] == 0:
                res.append(-1)
            else:
                res.append(distance[n1][n2])
        return res
    # =========================================
    
    # 2021/10/10 
    def calcEquation2(self, equations, values, queries):
        print("Code-2")
        graph = {}
        def build_graph(equations, values):
            def add_edge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1/value)
        
        def find_path(query):
            b, e = query
            
            if b not in graph or e not in graph:
                return -1.0
                
            q = collections.deque([(b, 1.0)])
            visited = set()
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]
    
    # =========================================

    # 2021/06/18
    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:    
        print("Code-1")
        
        # 題目
        print("equations: ", equations)
        print("values:", values)
        
        # 建構dataMap 
        # 從題目的條件預先處理所建構的圖，使用雙層hashmap，也就是 node -> {node -> rate} 的形式。
        # 在此我們還沒有得到任何新的資訊，只是把原本零散的邊組成一個給某點，就能得到相鄰點和rate的圖
        # Note: A點到A點也必須要存入1的值
        dataMap = self.buildDataMap(equations, values)
        print("dataMap:")
        for k, v in dataMap.items():
            print(" ", k, "->", [str(p) + "->" + str(q) for p, q in v.items()])
            
        # 建構pathMap
        # 使用DFS/BFS把圖遍歷，建立一個終點可以找到初始點的map，以及整條路的rate，也就是 des -> [src, pathRate]
        # Note: 因為圖可能是斷開的，所以必須要掃描所有的點來當src的候選人
        pathMap = self.buildPathMap(dataMap)
        print("pathMap:")
        for k, v in pathMap.items():
            print(" ", k, "->", v)
        
        # 建構queryValueList
        # 掃描queries，並且使用pathMap來找到兩個終點是否具有相同的src()。
        # 如果有，代表兩者在同一個相連圗上，兩者之間的rate就是兩條pathRate相除。
        # Note: 因為圖可能是斷開的，所以必須要掃描所有的點來當src的候選人
        queryValueList = self.buildQueryValueList(pathMap, queries)
        print("queryValueList:", queryValueList)
        return queryValueList

    def buildDataMap(self, equations, values):
        dataMap = defaultdict(lambda: defaultdict(dict))
        for i, (e1, e2) in enumerate(equations):
            dataMap[e1][e1] = 1
            dataMap[e2][e2] = 1
            dataMap[e1][e2] = values[i]
            dataMap[e2][e1] = 1 / values[i]
        return dataMap
        
    def buildPathMap(self, dataMap):
        pathMap = collections.defaultdict(list)
        for node in dataMap:
            if node in pathMap:
                continue
            self.dfs(node, node, dataMap, pathMap)
        return pathMap 
            
    def dfs(self, src, cur, dataMap, pathMap):      
        # dataMap: cur -> {dest -> rate} 
        # pathMap: dest -> [src, pathRate]
        for dest, rate in dataMap[cur].items():  
            if dest in pathMap:
                continue           
            if dest == cur:
                pathMap[dest].extend((src, 1))
            else:
                pathMap[dest].extend((src, rate * pathMap[cur][1]))
            self.dfs(src, dest, dataMap, pathMap)
            
    def buildQueryValueList(self, pathMap, queries):
        queryValueList = []
        for e1, e2 in queries:
            if e1 not in pathMap or e2 not in pathMap:
                queryValueList.append(-1)
            elif pathMap[e1][0] == pathMap[e2][0]:  #same map
                queryValueList.append(pathMap[e2][1] / pathMap[e1][1])
            else:
                queryValueList.append(-1)
        return queryValueList