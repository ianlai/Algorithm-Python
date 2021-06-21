from collections import defaultdict

class Solution:
    
    # DFS [O(n):82%]
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        print("DFS")
        if not isConnected: 
            return 0
        
        nodeMap = self.parse(isConnected)
        count = self.getCountByTraversal(nodeMap)
        return count
    
    def parse(self, matrix):
        nodeMap = defaultdict(list)  #node -> [nodes]
        #nodeMap = {}
        for i in range(len(matrix)):
            nodeMap[i] = []
            for j in range(len(matrix[0])):
                if i == j:
                    continue
                if matrix[i][j] == 0:
                    continue
                nodeMap[i].append(j)
                #nodeMap[j].append(i)
        return nodeMap
    
    def getCountByTraversal(self, nodeMap):
        visited = set([])
        count = 0
        for node in nodeMap:
            if node in visited:
                continue
            count += 1
            self.dfs(nodeMap, node, visited)
        return count
    
    def dfs(self, nodeMap, node, visited):
        # if node in visited:
        #     return
        for nextNode in nodeMap[node]:
            if nextNode in visited:
                continue
            visited.add(nextNode)
            self.dfs(nodeMap, nextNode, visited)
    
    # ====================================================
    # Union Find [O(n3):29%]
    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        print("Union Find")
        if not isConnected:
            return 0
        
        n = len(isConnected)
        parents = [-1] * n
        self.count = n
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i == j:
                    continue
                if isConnected[i][j] == 0:
                    continue
                # connected case
                if i < j:  #Speed up - 1 (one direction)  [40%]
                    self.union(parents, i, j)
        return self.count
    
    def union(self, parents, A, B):
        def find(A):
            if parents[A] == -1:
                return A
            return find(parents[A])
        
        headA = find(A)
        headB = find(B)
        if headA != headB: 
            parents[headB] = headA #union
            self.count -= 1