class Solution:
    
    # 2022/01/07
    #BFS; traverse the edges and put the two vertices into two set [O(E): 5%]
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        setA = set()
        setB = set()
        visited = set()
        
        connectedGraph = collections.defaultdict(set)
        for i, nodes in enumerate(graph):
            if not nodes:
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
            
            rootKey, rootSet = list(connectedGraph.items())[0]
            deq = collections.deque([(rootKey, node) for node in rootSet])

            #print(deq)
            layer = 0
            while deq:
                left = deq[0][0] #cur[0]
                #print("left:", left)
                for _ in range(len(deq)):
                    edge = deq.popleft()
                    _, right = edge[0], edge[1]
                    if edge in visited:
                        continue
                    visited.add(edge)

                    if layer % 2 == 0:
                        if left in setB or right in setA: 
                            return False
                        setA.add(left)
                        setB.add(right)
                    else:
                        if left in setA or right in setB: 
                            return False
                        setA.add(right)
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
                