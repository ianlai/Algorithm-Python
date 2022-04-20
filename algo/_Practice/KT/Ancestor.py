'''
  1    2    3
/  \  /      \
4    5        6
                \
                  7
Input definition: 
    {1,4} means 1 is parent of 4
------------------------------------------
Problem1: Find the nodes with 0 or 1 parents 

Input1: 
    [[1,4], [1,5], [2,5], [3,6], [6,7]]

Output1: 
    [1, 2, 3, 4, 6, 7]  //5 is not inside
------------------------------------------
Problem2: Check two nodes have common ancestor
Input2: 
    [[1,4], [1,5], [2,5], [3,6], [6,7]]
    4, 5
Output2: 
    True
------------------------------------------
Problem3: Find the furthest ancestor
Input3: 
    [[1,4], [1,5], [2,5], [3,6], [6,7]]
    7
Output3: 
    3
------------------------------------------
'''

import collections
def findNodesWithZeroOrOneParents(links):
    nodeToParents = collections.defaultdict(set)
    for parent, child in links:
        nodeToParents[child].add(parent)
        if parent not in nodeToParents:
            nodeToParents[parent] = set() #need this otherwise no-parent nodes are not in the map

    res = []
    for node, parents in nodeToParents.items():
        if len(parents) <= 1:
            res.append(node)
    return res

links = [[1,4], [1,5], [2,5], [3,6], [6,7]] 
print(findNodesWithZeroOrOneParents(links))

# =========================================

def dfs(graph, node, parents):
    if node in parents:
        return 
    parents.add(node)
    for nxt in graph[node]:
        dfs(graph, nxt, parents)

def findAncestors(graph, node):
    parents = set()
    dfs(graph, node, parents)
    return list(parents)

# DFS (not backtracking)
def checkCommonAncestor(links, node1, node2):
    nodeToParents = collections.defaultdict(set)
    for parent, child in links:
        nodeToParents[child].add(parent)
        if parent not in nodeToParents:
            nodeToParents[parent] = set()
    
    parentList1 = findAncestors(nodeToParents, node1)
    parentList2 = findAncestors(nodeToParents, node2)

    for parent1 in parentList1:
        if parent1 in parentList2:
            return True
    return False

print(checkCommonAncestor(links, 4, 2)) #False
print(checkCommonAncestor(links, 4, 5)) #True
print(checkCommonAncestor(links, 4, 1)) #True
print(checkCommonAncestor(links, 6, 1)) #False
print(checkCommonAncestor(links, 7, 3)) #True
print(checkCommonAncestor(links, 8, 3)) #False (8 not in graph)

# =========================================

#BFS: find the last node
def findFurthestAncestor(links, node):
    nodeToParents = collections.defaultdict(set)
    for parent, child in links:
        nodeToParents[child].add(parent)
        if parent not in nodeToParents:
            nodeToParents[parent] = set()
    
    deq = collections.deque([node])
    pop = None
    while deq:
        pop = deq.popleft()
        for nxt in nodeToParents[pop]:
            deq.append(nxt)
    return pop

print(findFurthestAncestor(links, 4)) #1
print(findFurthestAncestor(links, 5)) #1 or 2
print(findFurthestAncestor(links, 7)) #3