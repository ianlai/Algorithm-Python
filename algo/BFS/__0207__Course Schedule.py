class Solution:
    
    #Topologic sorting [O(n), 5%]
    #Note: Jiuzhang defines graph (vertex); while Leetcode defines the prerequisites (edge)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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