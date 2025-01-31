"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

        cur = node
        while cur.parent and cur.parent.val < cur.val:
            cur = cur.parent
        if cur.parent and cur.parent.val > cur.val:
            return cur.parent
        return None