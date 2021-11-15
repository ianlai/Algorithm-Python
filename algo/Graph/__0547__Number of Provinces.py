from collections import defaultdict

class Solution:
    
    # Quiz-323
    # DFS 
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        print("Method-3")
        def countComponents(n: int, edges: List[List[int]]) -> int:
            def buildGraph(edges):
                graphMap = collections.defaultdict(list)
                for n1, n2 in edges:
                    graphMap[n1].append(n2)
                    graphMap[n2].append(n1)
                return graphMap

            def countGraph(n, graphMap):
                visited = set()
                count = 0
                for i in range(n):
                    if i not in graphMap:  #node is not in edges 
                        count += 1 
                        continue
                    if i in visited:
                        continue
                    count += 1
                    visited.add(i)
                    traverseDfs(i, graphMap, visited)
                return count 

            def traverseDfs(src, graphMap, visited):
                for dest in graphMap[src]:
                    if dest in visited:
                        continue 
                    visited.add(dest)
                    traverseDfs(dest, graphMap, visited)

            if n == 0:
                return 0
            graphMap = buildGraph(edges)
            count = countGraph(n, graphMap)
            return count 
        
        edges = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i >= j:
                    continue
                if isConnected[i][j] == 1:
                    edges.append([i, j])
        #print(edges)
        res = countComponents(len(isConnected), edges)
        return res
    
    # ====================================================
    # DFS [O(n):82%]
    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
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