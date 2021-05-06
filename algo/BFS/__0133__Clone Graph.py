"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        mydeq = collections.deque([node])
        myset = set([node])
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        
        # New nodes ; Add node mappings between old nodes and new nodes
        while mydeq:
            cur = mydeq.popleft()
            for neighbor in cur.neighbors:
                if neighbor in myset:
                    continue
                mydeq.append(neighbor)
                myset.add(neighbor)
                oldToNew[neighbor] = Node(neighbor.val)  #add old to new mapping
        
        # Debug
        # for old in oldToNew.keys():
        #     new = oldToNew[old]
        #     print(old.val, id(old), "--", new.val, id(new))
        
        # Add edge mappings between old nodes and new nodes
        mylist = list(myset)
        for old in oldToNew.keys():
            if not old.neighbors:
                continue
            new = oldToNew[old]            
            new.neighbors = []
            for oldNeighbor in old.neighbors:
                #print(oldNeighbor.val)
                newNeighbor = oldToNew[oldNeighbor]
                new.neighbors.append(newNeighbor)
                
        return oldToNew[node]