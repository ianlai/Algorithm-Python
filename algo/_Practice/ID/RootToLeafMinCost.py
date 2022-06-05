'''
Roof To Leaf Min Cost

(1) Tree
(2) DAG

'''

edges = [["A", "B", 3], ["A", "C", 2], ["B", "D", 1], ["C", "D", 4], ["D", "F", 8], ["D", "E", 2],  ["E", "F", 3]]

import collections
import math
def parse(edges):
    graph = collections.defaultdict(dict)
    nodes = set()
    leaves = set()
    outNodes = set()
    for v1, v2, e in edges:
        graph[v1][v2] = e 
        nodes.add(v1)
        nodes.add(v2)
        outNodes.add(v1)

    for node in list(nodes):
        if node not in outNodes:
            leaves.add(node)
    return graph, leaves 

'''
distance 是從尾巴開始補回來的 
但path卻是從前面過去的 兩者對不上 只能找最小distance 
'''
def findMinCost(graph, root):
    print("Code1")
    res = []
    distToEnd = {}
    dfs1(graph, root, res, [root], distToEnd)
    print(distToEnd)
    return distToEnd[root]
 
def dfs1(graph, node, res, path, distToEnd):
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
def findMinPath(graph, root):
    print("Code-2")
    res = []
    print("Target:", root)
    distFromRoot = {root: 0}
    dfs2(graph, root, res, [root], distFromRoot)
    print(distFromRoot)
    return distFromRoot[root]
 
def dfs2(graph, node, res, path, distFromRoot):
    if node not in graph:  #leaf
        return 

    for nxt, cost in graph[node].items():
        path.append(nxt)
        print(node, "->", nxt, ":", cost, distFromRoot)
        if nxt not in distFromRoot:
            distFromRoot[nxt] = cost
        else:
            distFromRoot[nxt] = min(distFromRoot[nxt], distFromRoot[node] + cost)  # relax
        dfs2(graph, nxt, res, path, distFromRoot)
        path.remove(nxt)
    return 


graph, leaves = parse(edges)
print("Graph: ", graph)
print("Leaves: ", leaves)

#Pass head (to end)
print(findMinCost(graph, "A"))

#Pass end (from start)
print(findMinPath(graph, "A"))