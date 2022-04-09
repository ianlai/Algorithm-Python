import heapq
class Solution:
    
    # 2022/04/09 
    # DFS 使用大神的方法，重點是要先把資料整理好。做出有序的map後，使用backtracking找到的第一個就是解 
    # [time: O(E + VlogV + E^d), d is max edge of one node: 34% / space: O(V + E)]
    def findItinerary(self, tickets):
        print("Code2")
        
        #src -> dst -> ticketNum
        def generateLinkMap(tickets):
            graph = collections.defaultdict(lambda: collections.defaultdict(int))
            for v1, v2 in tickets:
                graph[v1][v2] += 1
            return graph
        
        #src -> (dst, ticketNum), sorted by dst
        def genereateOrderedMap(graph):
            orderedMap = collections.defaultdict(list) 
            for src in graph.keys():
                dstList = []
                for dst in sorted(graph[src].keys()):
                    dstList.append([dst, graph[src][dst]]) 
                orderedMap[src] = dstList
            return orderedMap 
        
        def dfs(graph, cur, path, remaining):
            if remaining == 0:
                return path
            if cur not in graph:
                return None
            
            for idx in range(len(graph[cur])):
                nxt, nxtRemaining = graph[cur][idx] #dst, tickets
                if nxtRemaining == 0:
                    continue
                graph[cur][idx] = [nxt, nxtRemaining-1]
                res = dfs(graph, nxt, path + [nxt], remaining-1)
                if res:
                    return res
                graph[cur][idx] = [nxt, nxtRemaining] #backtracking
            return None 
        
        linkMap = generateLinkMap(tickets)
        dstOrderedMap = genereateOrderedMap(linkMap)
        
        start = "JFK"
        path = [start]
        res = dfs(dstOrderedMap, start, path, len(tickets))
        return res

    # =====================================================

    # Backtracking; finish all edges (not nodes) [O(V+E): 50%]
    def findItinerary2(self, tickets):
        print("大神")
        graph = self.buildGraph(tickets)
        print(graph)
        return self.dfs(graph, "JFK", ["JFK"], len(tickets))
    
    def buildGraph(self, tickets):
        graph = collections.defaultdict(lambda: defaultdict(int))
        for src, dsc in tickets:
            graph[src][dsc] += 1

        ordered_graph = {}
        for src in graph:
            ordered_graph[src] = []
            for dsc in sorted(graph[src].keys()):
                ordered_graph[src].append([dsc, graph[src][dsc]])
        return ordered_graph

    def dfs(self, graph, src, path, depth):
        if depth == 0:
            return path
        
        if src not in graph:
            return None
        
        for idx in range(len(graph[src])):
            dsc, remain = graph[src][idx]
            if remain > 0:
                graph[src][idx][1] -= 1 # update remain
                path.append(dsc)

                result = self.dfs(graph, dsc, path, depth - 1)
                if result is not None:
                    return result

                path.pop()
                graph[src][idx][1] += 1
        return None

    # =====================================================
    
    # 2021/07/07
    # Backtracking; finish all edges (not nodes) [O(V+E): 38%]
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        
        self.numRemainingTickets = 0
        srcToDsts, srcToUseds = self.parse(tickets)
        print(srcToDsts)
        path = ["JFK"]
        self.traverse(srcToDsts, srcToUseds, "JFK", path)
        return path
        
    def parse(self, tickets):
        
        srcToDsts = collections.defaultdict(list)  #JFK -> [SFO, ATL]
        srcToUseds = collections.defaultdict(list) #JFK -> [used, unused]
        
        for src, dst in tickets:  
            if len(srcToDsts[src]) == 0:
                srcToDsts[src].append(dst)
                srcToUseds[src].append(False)
            else:   #keep the lexical order
                isAdded = False
                for i in range(len(srcToDsts[src])):
                    if dst < srcToDsts[src][0] or (i > 0 and srcToDsts[src][i-1] <= dst < srcToDsts[src][i]):
                        srcToDsts[src].insert(i, dst)
                        srcToUseds[src].insert(i, False)
                        isAdded = True
                        break
                        
                if not isAdded:
                    srcToDsts[src].append(dst)
                    srcToUseds[src].append(False)     
            self.numRemainingTickets += 1
        
        return srcToDsts, srcToUseds
    
    def traverse(self, srcToDsts, srcToUseds, src, path):
        if self.numRemainingTickets == 0:
            #print(src, path, self.numRemainingTickets, "###")
            return True
        
        size = len(srcToDsts[src])
        for i in range(size):
            if srcToUseds[src][i]:
                continue

            dst = srcToDsts[src][i]
            srcToUseds[src][i] = True
            path.append(dst)

            self.numRemainingTickets -= 1
            if self.traverse(srcToDsts, srcToUseds, dst, path):
                return True
            
            #path.remove(dst) #remove first one 
            idx = path[::-1].index(dst)  
            path.pop(len(path) - idx - 1)  #remove last one
            
            srcToUseds[src][i] = False
            self.numRemainingTickets += 1