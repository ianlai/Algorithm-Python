# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 2022/01/06
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def generateGraph(graph, node, parent):
            if node.left:
                graph[node].add(node.left)
                generateGraph(graph, node.left, node)
            if node.right:
                graph[node].add(node.right)
                generateGraph(graph, node.right, node)
            if parent:
                graph[node].add(parent)
                
        def findDistanceNodes(graph, target, k):
            deq = collections.deque([target])
            distanceNodes = []
            visited = set()
            while deq:
                for _ in range(len(deq)):
                    cur = deq.popleft()
                    if cur in visited:
                        continue
                    visited.add(cur)
                    for nxt in graph[cur]:
                        deq.append(nxt)
                    if k == 0:
                        distanceNodes.append(cur.val)
                if k == 0:     
                    break
                k -= 1
            return distanceNodes
        
        graph = collections.defaultdict(set)
        generateGraph(graph, root, None) #DFS
        res = findDistanceNodes(graph, target, k) #BFS
        return res 
    
    # =========================================================
    
    # 2021/05/17
    # Transform to graph ; BFS in graph [O(n), 42%]
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        self.graph = {}
        self.transform(root, None) 
        
        #=== Debug ===
        #self.debugGraph()
        
        result = []
        self.bfs(target, k, result)
        return result
    
    def transform(self, root, parent):
        if not root:
            return 
        self.graph[root] = []
        if root.left: 
            self.graph[root].append(root.left)
        if root.right:
            self.graph[root].append(root.right)
        if parent:
            self.graph[root].append(parent)  #record the parent 
            
        self.transform(root.left, root)
        self.transform(root.right, root)
    
    def bfs(self, target, k, result):
        visited = set()
        deq = collections.deque([target])
        layer = 0
        while deq:
            
            #=== Debug ===
            #print("Layer-" + str(layer) + ":")
            #self.debugDeque(deq)
            
            for _ in range(len(deq)):
                cur = deq.popleft()
                visited.add(cur)
                if layer == k:
                    result.append(cur.val)
                for node in self.graph[cur]:
                    if node in visited:
                        continue
                    deq.append(node)
            layer += 1
        return 

    def debugGraph(self):
        for node in self.graph:
            self.debugNode(node)
            
    def debugDeque(self, deq):
        for node in deq:
            self.debugNode(node)
        
    def debugNode(self, node):
        print( " " +str(node.val) + " -> " + str([node.val for node in self.graph[node]]))
            