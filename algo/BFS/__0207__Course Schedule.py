class Solution:
    
    # 2021/11/14
    # BFS (Topological sorting) [O(n): 97%]
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("Code-2")
        if not prerequisites or not numCourses:
            return True
        nToNext = self.buildMap(numCourses, prerequisites)
        starts = [n for n in nToNext if nToNext[n][0] == 0]
        numDone = len(starts)
        
        #print(nToNext)
        #print("starts:", starts)
        deq = collections.deque(starts)
        while deq:
            cur = deq.popleft()
            for nxt in nToNext[cur][1]:
                nToNext[nxt][0] -= 1 
                if nToNext[nxt][0] == 0:
                    deq.append(nxt)
                    numDone += 1
                    
        #print(nToNext)   
        if numDone == numCourses:
            return True
        return False
            
    def buildMap(self, numCourses, prerequisites):
        nToNext = collections.defaultdict(list)
        for n in range(numCourses):
            nToNext[n] = [0, []]
        for nxt, cur in prerequisites:
            nToNext[nxt][0] += 1        #indegree
            nToNext[cur][1].append(nxt) #out course
        return nToNext
            
    #=================================================
        
    # 2021/05/09
    # Topological sorting [O(n), 5%]
    # Note: Jiuzhang defines graph (vertex); while Leetcode defines the prerequisites (edge)
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("Code-1")
        if not prerequisites or not numCourses:
            return True
        
        nodeToIndegree = self.getIndegree(prerequisites)
        startNodes = [node for node in nodeToIndegree if nodeToIndegree[node] == 0]
        deq = collections.deque(startNodes)
        
        while deq: 
            cur = deq.popleft()
            for pair in prerequisites:
                #Find all nodes which needs the cur as the prerequisite
                if pair[1] == cur: 
                    nodeToIndegree[pair[0]] -= 1     #Since cur will be removed, we can minus the found node's indegree by 1
                    if nodeToIndegree[pair[0]] == 0: #Add the node into deque if the indegree becomes 0
                        deq.append(pair[0])
                        
        #If any node showing in prerequisites still not 0-degree, this means this node can't be erased, return False
        countNotZeroIndegree = 0
        for node in nodeToIndegree:
            if nodeToIndegree[node] != 0:
                return False
        return True
    
    #Traverse the prerequisites, count the indegress of all nodes including 0-indegree nodes 
    def getIndegree(self, prerequisites):
        nodeToIndegree = {}
        for pair in prerequisites:
            #Case for nodes with 0 indegree
            if pair[1] not in nodeToIndegree:
                nodeToIndegree[pair[1]] = 0
            #Case for nodes with more-than-1 degree
            if pair[0] in nodeToIndegree:
                nodeToIndegree[pair[0]] += 1
            else:
                nodeToIndegree[pair[0]] = 1
        return nodeToIndegree