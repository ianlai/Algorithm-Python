"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    # 2022/04/12
    # BFS [O(n): 23%]
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        deq = collections.deque([root])
        while deq:
            cur = []
            for _ in range(len(deq)):
                pop = deq.popleft()
                cur.append(pop.val)
                deq.extend(pop.children)
            res.append(cur)
        return res