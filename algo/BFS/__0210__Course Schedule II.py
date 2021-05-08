class Solution:
    
    #Topological sorting [O(n), 5%]
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                