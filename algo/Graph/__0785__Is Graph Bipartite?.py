class Solution:
    
    # 2022/01/08
    # DFS to mark the colors [O(V+E): 18%]
    def isBipartite(self, graph: List[List[int]]) -> bool:
        print("Code5: DFS")
        colorMap = {}
        def dfs(graph, colorMap, node, color):
            colorMap[node] = color
            for nxt in graph[node]:
                if nxt in colorMap:
                    if colorMap[node] == colorMap[nxt]:
                        return False
                else:
                    if not dfs(graph, colorMap, nxt, color ^ 1):
                        return False
            return True
        
        for node in range(len(graph)):
            if node in colorMap:
                continue
            if not dfs(graph, colorMap, node, 0): #new start will be marked as 0
                return False
        return True

    # =================================
    
    # 2022/01/08
    # 錯的，不是把邊全部掃過一遍來填兩端就可以，填色是有順序的，否則會誤判為False
    # e.g. [0-3-4-1-2] 
    # 如果我們先填0-3為A/B，再填1-2為A/B就會造成4無法填入，但其實1-2應該填為B/A就可以
    def isBipartite4(self, graph: List[List[int]]) -> bool:
        print("Code4: Generate edgeList")
        edges = []
        for v1, nodes in enumerate(graph):
            for v2 in nodes:
                if v2 < v1:
                    continue
                edges.append((v1, v2))
        print(edges)
        nodeToColor = {}
        for v1, v2 in edges:
            print(nodeToColor)
            if v1 not in nodeToColor and v2 not in nodeToColor:
                nodeToColor[v1] = 0
                nodeToColor[v2] = 1
            elif v2 not in nodeToColor:
                nodeToColor[v2] = nodeToColor[v1] ^ 1
            elif v1 not in nodeToColor:
                nodeToColor[v1] = nodeToColor[v2] ^ 1    
            else:
                if nodeToColor[v1] == nodeToColor[v2]:
                    return False
        return True
    
    # =================================
    
    # 2022/01/08
    #BFS; traverse the edges and use nodeToColor map to record the color [O(V+E): 5%]
    def isBipartite3(self, graph: List[List[int]]) -> bool:
        print("Code3: Traverse the edges, slow")
        
        visited = set() #edge
        nodeToColor = {}
        
        #Construct the connected graphs (possible to have multiple connected graphs)
        connectedGraph = collections.defaultdict(set)
        for i, nodes in enumerate(graph):
            if not nodes:  #Not need to consider the isolated nodes 
                continue
            for node in nodes:
                connectedGraph[i].add(node)
        
        # Multiple connected graphs exist
        # Remove the traversed nodes until the graph empty
        while connectedGraph:
            
            #Since we are using defaultdict, the new set will be created
            #Need to consider the empty set also should be considered as empty
            isEmptyGraph = True
            for key, vset in connectedGraph.items():
                if len(vset) != 0:
                    isEmptyGraph = False
                    break
            if isEmptyGraph:
                break
            
            #Each round we will do BFS in a connected graph 
            rootKey, rootSet = next(iter(connectedGraph.items()))
            deq = collections.deque([(rootKey, node) for node in rootSet])
            layer = 0
            while deq:
                for _ in range(len(deq)):
                    edge = deq.popleft()
                    left, right = edge[0], edge[1]
                    if edge in visited:
                        continue
                    visited.add(edge)

                    if layer % 2 == 0:
                        if left in nodeToColor and nodeToColor[left] == 1:
                            return False
                        if right in nodeToColor and nodeToColor[right] == 0 :
                            return False
                        nodeToColor[left] = 0
                    else:
                        if left in nodeToColor and nodeToColor[left] == 0:
                            return False
                        if right in nodeToColor and nodeToColor[right] == 1 :
                            return False
                        nodeToColor[left] = 1

                    for nxt in connectedGraph[right]:
                        deq.append((right, nxt))
                
                del connectedGraph[left] 
                layer += 1
        return True
    
    # =================================
    
    # 2022/01/07
    #BFS; traverse the edges and put the two vertices into two set [O(V+E): 5%]
    def isBipartite2(self, graph: List[List[int]]) -> bool:
        print("Code2: Traverse the edges, slow")
        
        setA = set() #node
        setB = set() #node
        visited = set() #edge
        
        #Construct the connected graphs (possible to have multiple connected graphs)
        connectedGraph = collections.defaultdict(set)
        for i, nodes in enumerate(graph):
            if not nodes:  #Not need to consider the isolated nodes 
                continue
            for node in nodes:
                connectedGraph[i].add(node)
        
        while connectedGraph:
            print("==============")
            #print(connectedGraph)
            
            isEmptyGraph = True
            for key, vset in connectedGraph.items():
                if len(vset) != 0:
                    isEmptyGraph = False
                    break
            if isEmptyGraph:
                break
            
            rootKey, rootSet = next(iter(connectedGraph.items()))
            deq = collections.deque([(rootKey, node) for node in rootSet])

            #print(deq)
            layer = 0
            while deq:
                for _ in range(len(deq)):
                    edge = deq.popleft()
                    left, right = edge[0], edge[1]
                    if edge in visited:
                        continue
                    visited.add(edge)

                    if layer % 2 == 0:
                        if left in setB or right in setA: 
                            return False
                        setA.add(left)
                    else:
                        if left in setA or right in setB: 
                            return False
                        setB.add(left)

                    for nxt in connectedGraph[right]:
                        deq.append((right, nxt))
                
                del connectedGraph[left] 
                layer += 1
                #print(setA, setB)
        return True
    
    # =================================
    # BFS; traverse the nodes; Incorrect 
    def isBipartite1(self, graph: List[List[int]]) -> bool:
        print("Code1: Traverse the nodes, incorrect")
        setA = set()
        setB = set()
        visited = set()
        
        deq = collections.deque([0])
        layer = 0
        while deq:
            for _ in range(len(deq)):
                cur = deq.popleft()
                if cur in visited:
                    continue
                visited.add(cur)
                if layer % 2 == 0:
                    if cur in setB:
                        return False
                    setA.add(cur)
                else:
                    if cur in setA:
                        return False
                    setB.add(cur)
                for nxt in graph[cur]:  
                    deq.append(nxt)
            layer += 1
        print(setA, setB)
        return True
                