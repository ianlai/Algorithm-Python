'''
Roof To Leaf Min Cost

Given a tree,(binary tree possibily) every tree edge has a cost， find the least
cost or find the leaf node that the cost of path that from root to leaf is the
least.
Follow Up:
如果不是binary tree的结构，而是任意的DAG，问代码还是否work（yes）
有没有优化的地方？（用hashmap存下每个节点到叶节点的distance，这样再次访问到该叶节点就不必dfs下去）。
时间复杂度？优化之前是O(V!)优化之后是O(V+E)
BFS也要做些一下//我用DFS做，面试官说改成bfs优化一下，我就没弄出来
http://www.1point3acres.com/bbs/thread-230257-1-1.html

(1) Tree
- DFS: O(N)  //V = E

(2) DAG
- DFS: O(V!) or O(V^e) (e: 每個node的邊數)
- Memoization: O(V+E)  // 看起來是碰到V退出，但其實是DFS-Post，所以所有的邊都必須要走過
'''

#Tree
tree = [["A", "B", 3], ["A", "C", 2], ["B", "D", 4], ["B", "E", 8], ["B", "F", 5], ["E", "J", 1], ["E", "K", 2],  ["C", "G", 1],  ["G", "H", 2], ["G", "I", 3]]

#Graph 
edges = [["A", "B", 3], ["A", "C", 2], ["B", "D", 1], ["C", "D", 4], ["D", "F", 8], ["D", "E", 2],  ["E", "F", 3], ["E", "G", 4]]
edges2 = [["E", "G", 3], ["G", "J", 2], ["H", "G", 1], ["H", "J", 4], ["H", "I", 5], ["I", "J", 3],  ["E", "I", 2], 
["D", "E", 2], ["D", "G", 9], ["B", "D", 4], ["F", "E", 1], ["F", "I", 5], ["C", "F", 1],  ["C", "E", 6], ["C", "B", 3], ["A", "C", 2], ["A", "B", 1]]


import collections
import math

def parse(edges):
    graph = collections.defaultdict(dict)
    for v1, v2, e in edges:
        graph[v1][v2] = e 
    return graph

'''
distance 是從尾巴開始補回來的 
但path卻是從前面過去的 兩者對不上 只能找最小distance 
'''
def findMinCost(graph, root):
    print("==== DFS-Post (with Memoization) ====")
    res = []
    distToEnd = {}
    #dfs1(graph, root, res, [root], distToEnd)
    dfs1(graph, root, distToEnd)
    print(distToEnd)
    return distToEnd[root]
 
'''
從尾做就是DFS-Post (從leaf開始往上建)
'''
def dfs1(graph, node, distToEnd):
    if node not in graph:  #leaf
        return 0
    if node in distToEnd:
        return distToEnd[node]
    totalCost = math.inf
    for nxt, cost in graph[node].items():
        totalCost = min(totalCost, cost + dfs1(graph, nxt, distToEnd))
    distToEnd[node] = totalCost  #memoization DP
    return totalCost

# 嘗試想要backtracking（還沒成功）
def dfs1_backtracking(graph, node, res, path, distToEnd):
    if node not in graph:  #leaf
        return 0
    if node in distToEnd:
        return distToEnd[node]
    totalCost = math.inf
    for nxt, cost in graph[node].items():
        path.append(nxt)
        #print(node, "->", nxt, ":", cost, path)
        totalCost = min(totalCost, cost + dfs1(graph, nxt, res, path, distToEnd))
        path.remove(nxt)
    distToEnd[node] = totalCost  #memoization DP
    return totalCost

'''
從前到後的作法 [Incorrect]
'''
# def findMinPath(graph, root):
#     print("Code-2")
#     res = []
#     print("Target:", root)
#     distFromRoot = {root: 0}
#     dfs2(graph, root, res, [root], distFromRoot)
#     print(distFromRoot)
#     return distFromRoot[root]
 
# def dfs2(graph, node, res, path, distFromRoot):
#     if node not in graph:  #leaf
#         return 

#     for nxt, cost in graph[node].items():
#         path.append(nxt)
#         print(node, "->", nxt, ":", cost, distFromRoot)
#         if nxt not in distFromRoot:
#             distFromRoot[nxt] = cost
#         else:
#             distFromRoot[nxt] = min(distFromRoot[nxt], distFromRoot[node] + cost)  # relax
#         dfs2(graph, nxt, res, path, distFromRoot)
#         path.remove(nxt)
#     return 


'''
從頭做就要不斷更新，所以用Dijkstra
用這方法最後要去找出leaf nodes們，看哪一個距離最小。
'''
import heapq
def findMinDijkstra(graph, root):
    print("==== Dijkstra ====")
    distance = collections.defaultdict(lambda: math.inf)
    distance[root] = 0
    heap = [(0, root)]  #distance, node
    while heap:
        d, cur = heapq.heappop(heap)
        distance[cur] = min(distance[cur], d)
        for nxt, curToNext in graph[cur].items():
            if distance[cur] + curToNext < distance[nxt]:
                heapq.heappush(heap, (distance[cur] + curToNext, nxt)) 
    print("Dijkstra:", distance)


#Pass head (to end)
# tree = parse(tree)
# print("Tree: ", tree)
# print(findMinCost(tree, "A"))

# ===================================

graph = parse(edges)
print("Graph: ", graph)
print(findMinCost(graph, "A"))

findMinDijkstra(graph, "A")

# ===================================

# graph2 = parse(edges2)
# print("Graph: ", graph2)
# print(findMinCost(graph2, "A"))


# #Pass end (from start)
# print(findMinPath(graph, "A"))