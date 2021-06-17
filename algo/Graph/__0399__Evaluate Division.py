class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:    
        
        # 題目
        print("equations: ", equations)
        print("values:", values)
        
        # 建構dataMap 
        # 從題目的條件預先處理所建構的圖，使用雙層hashmap，也就是 node -> {node -> rate} 的形式。
        # 在此我們還沒有得到任何新的資訊，只是把原本零散的邊組成一個給某點，就能得到相鄰點和rate的圖
        # Note: A點到A點也必須要存入1的值
        dataMap = self.buildDataMap(equations, values)
        print("dataMap:", [d for d in dataMap.items()])
        
        # 建構pathMap
        # 使用DFS/BFS把圖遍歷，建立一個終點可以找到初始點的map，以及整條路的rate，也就是 des -> [src, pathRate]
        # Note: 因為圖可能是斷開的，所以必須要掃描所有的點來當src的候選人
        pathMap = self.buildPathMap(dataMap)
        print("pathMap:", pathMap)
        
        # 建構queryValueList
        # 掃描queries，並且使用pathMap來找到兩個終點是否具有相同的src()。
        # 如果有，代表兩者在同一個相連圗上，兩者之間的rate就是兩條pathRate相除。
        # Note: 因為圖可能是斷開的，所以必須要掃描所有的點來當src的候選人
        queryValueList = self.buildQueryValueList(pathMap, queries)
        print("queryValueList:", queryValueList)
        return queryValueList

    def buildDataMap(self, equations, values):
        dataMap = {}
        for i in range(len(equations)):
            e1, e2 = equations[i][0], equations[i][1]
            if e1 not in dataMap:
                dataMap[e1] = {}
                dataMap[e1][e1] = 1
            if e2 not in dataMap:
                dataMap[e2] = {}
                dataMap[e2][e2] = 1
            dataMap[e1][e2] = values[i]
            dataMap[e2][e1] = 1 / values[i]
        return dataMap
        
    def buildPathMap(self, dataMap):
        pathMap = {}
        for node in dataMap:
            print("======= Head:", node)
            if node in pathMap:
                continue
            self.dfs(node, node, dataMap, pathMap)
        return pathMap 
            
    def dfs(self, src, cur, dataMap, pathMap):
        
        # if cur in pathMap:
        #     return
        
        # dataMap: cur -> {dest -> rate} 
        # pathMap: dest -> [src, pathRate]
        for dest, rate in dataMap[cur].items(): 
            
            # dest not in pathMap
            if dest not in pathMap:
                pathMap[dest] = []
                
            # dest in pathMap
            if len(pathMap[dest]) == 2: #exit
                continue
            
            pathMap[dest].append(src)
            if dest == cur:
                pathMap[dest].append(1)
            else:
                pathMap[dest].append(rate * pathMap[cur][1])
            self.dfs(src, dest, dataMap, pathMap)
            
    def buildQueryValueList(self, pathMap, queries):
        queryValueList = []
        for e1, e2 in queries:
            if e1 not in pathMap or e2 not in pathMap:
                queryValueList.append(-1)
                continue
            if pathMap[e1][0] == pathMap[e2][0]:  #same map
                queryValueList.append(pathMap[e2][1] / pathMap[e1][1])
            else:
                queryValueList.append(-1)
        return queryValueList