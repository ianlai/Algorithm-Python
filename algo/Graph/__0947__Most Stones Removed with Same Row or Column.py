class Solution:
    
    #2022/03/04
    #DFS，complicated for generating the graph [O(n), n is len(stones): 49%]
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def generateGraphgenerateGraph(stones):
            fromMap = collections.defaultdict(set)
            toMap = collections.defaultdict(set)
            graph = collections.defaultdict(set)
            
            #create nodes
            for i, stone in enumerate(stones):
                fromMap[stone[0]].add(i)
                toMap[stone[1]].add(i)
            
            #link the nodes
            for i, stone in enumerate(stones):
                for v in list(fromMap[stone[0]]):
                    if v != i:
                        graph[i].add(v)
                for v in list(toMap[stone[1]]):
                    if v != i:
                        graph[i].add(v)
                        
            return graph
        
        def dfs(node, visited, cur):
            if node in visited:
                return
            visited.add(node)
            cur.add(node)
            for nextNode in graph[node]:
                dfs(nextNode, visited, cur)            
    
        graph = generateGraphgenerateGraph(stones)
        maxStep = 0
        visited = set()
        for node in graph.keys():
            if node in visited:
                continue
            cur = set()
            dfs(node, visited, cur)
            maxStep += len(cur) - 1
        return maxStep