class Solution:
    
    # 2021/11/14
    # Topological sorting [O(n), 70%]
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("Code-3")
        if not numCourses:
            return []
        
        nToNext = self.buildMap(numCourses, prerequisites)
        starts = [n for n in nToNext if nToNext[n][0] == 0]
        res = []
        #print("starts:", starts)
        deq = collections.deque(starts)
        while deq:
            cur = deq.popleft()
            res.append(cur)
            for nxt in nToNext[cur][1]:
                nToNext[nxt][0] -= 1 
                if nToNext[nxt][0] == 0:
                    deq.append(nxt)
        #print(res)
        if len(res) == numCourses:
            return res
        return []
            
    def buildMap(self, numCourses, prerequisites):
        nToNext = collections.defaultdict(list)
        for n in range(numCourses):
            nToNext[n] = [0, []]
        for nxt, cur in prerequisites:
            nToNext[nxt][0] += 1        #indegree
            nToNext[cur][1].append(nxt) #out course
        return nToNext
    
    # =======================================================
    
    # 2021/06/21
    # Topological sorting [O(n), 64%]
    # nodeToIndegree: node -> indegree (int)
    # nodeToNextList: node -> nextList (list)  //faster if we have this since we can avoid scanning prerequisites again and again 
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("Code-2")
        if not numCourses:
            return []
        
        nodeToIndegree, nodeToNextList = self.parse(numCourses, prerequisites) 
        print(nodeToIndegree, nodeToNextList)
        zeroIndegreeNodes = [x for x in nodeToIndegree if nodeToIndegree[x] == 0]
        results = []
        
        #BFS 
        deque = collections.deque(zeroIndegreeNodes) 
        while deque:
            cur = deque.popleft()
            #print(cur)
            results.append(cur)
            for child in nodeToNextList[cur]:
                nodeToIndegree[child] -= 1
                #print(cur, "-", child)
                if nodeToIndegree[child] == 0:
                    deque.append(child)
        #print(results)
        return results if len(results) == numCourses else []
    
    def parse(self, num, pairs):
        
        n2i = collections.defaultdict(int)
        n2n = collections.defaultdict(list)
        # parse (using defaultdict makes logic cleaner)
        for dst, src in pairs:
            n2i[dst] += 1
            n2n[src].append(dst)
        
        # add isolated nodes 
        for i in range(num):
            if i not in n2i:
                n2i[i] = 0
            if i not in n2n:
                n2n[i] = []
        
        return n2i, n2n
        
    # =======================================================
    # 2021/05/08
    # Topological sorting, slow [O(n), 5%]
    # nodeToIndegree: node -> indegree (int)
    def findOrder1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        print("Code-1")
        if not numCourses: 
            return []
        
        # All nodes are independent 
        if not prerequisites:
            order = []
            for i in range(numCourses):
                order.append(i)
            return order
            
        nodeToIndegree = self.getIndegree(prerequisites)
        startNodes = [n for n in nodeToIndegree if nodeToIndegree[n] == 0]
        deque = collections.deque(startNodes)
        order = []
        
        while deque:
            cur = deque.popleft()
            order.append(cur)
            for p in prerequisites:
                if p[1] == cur: 
                    nodeToIndegree[p[0]] -= 1
                    if nodeToIndegree[p[0]] == 0:
                        deque.append(p[0])
        
        # No route     
        countNotZero = 0
        for node in nodeToIndegree:
            if nodeToIndegree[node] != 0:
                return []
        
        # Has route; fill in the isolated nodes 
        for i in range(numCourses):
            if i not in order:
                order.append(i)
        return order
    
    def getIndegree(self, prerequisites):
        nodeToIndegree = {}
        for p in prerequisites:
            if p[1] not in nodeToIndegree:
                nodeToIndegree[p[1]] = 0
            if p[0] not in nodeToIndegree:
                nodeToIndegree[p[0]] = 1
            else:
                nodeToIndegree[p[0]] += 1
        return nodeToIndegree
                