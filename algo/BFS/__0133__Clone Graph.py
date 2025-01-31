"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    # 2021/11/24
    # BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        deq = collections.deque([node])
        visited = set([node])
        curToNew = {}
        
        #BFS to clone node and mapping
        while deq:
            curNode = deq.popleft()
            
            newNode = Node(curNode.val) #node
            curToNew[curNode] = newNode #mapping
            
            for neighbor in curNode.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                deq.append(neighbor)
        
        
        #BFS again to clone the edges 
        deq = collections.deque([node])
        visited = set([node])
        while deq:
            curNode = deq.popleft()
            newNode = curToNew[curNode]
            for neighbor in curNode.neighbors:
                newNode.neighbors.append(curToNew[neighbor])
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                deq.append(neighbor)
                
        return curToNew[node]
    
    
    # 2021/05/07 
    # BFS 
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