class Solution:
    
    # 2022/04/08  
    # DFS [O(2^V): 57%]
    # 類似Subset題，加上一個點之後，可以分成原本的路徑和包含該點路徑，直接變兩倍
    # 因為是DAG，沒有環，所以不需要visited
    
    #加入nxt，開頭要先放一個
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        print("Code3")
        def dfs(node, dest, cur, res):
            if node == dest:
                res.append(list(cur))
                return 
            for nxt in graph[node]:
                dfs(nxt, dest, cur + [nxt], res)
    
        dest = len(graph) - 1
        res = []
        dfs(0, dest, [0], res) #開頭
        return res
        
    #加入cur，最後要補一個
    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        print("Code2")
        def dfs(node, dest, cur, res):
            if node == dest:
                res.append(list(cur + [node]))  #最後
                return 
            cur.append(node)
            for nxt in graph[node]:
                dfs(nxt, dest, cur, res)
            cur.remove(node)
        
        dest = len(graph) - 1
        res = []
        dfs(0, dest, [], res)
        return res
    
    # 2021/06/18 
    # DFS on Graph, backtracking [O(2^E), 31%]
    def allPathsSourceTarget1(self, graph: List[List[int]]) -> List[List[int]]:
        print("Code1")
        if not graph or not graph[0]:
            return []
        
        visited = set([])
        n = len(graph)
        result = []
        self.traverse(graph, n, 0, [0], result, visited)
        return result
        
    def traverse(self, graph, n, node, cur, result, visited):
        if node == n - 1:
            result.append(cur)
            return 
        
        for nextNode in graph[node]:
            #if nextNode in visited: 
            #    continue
            #visited.add(nextNode)
            self.traverse(graph, n, nextNode, cur + [nextNode], result, visited)
            #visited.remove(nextNode)