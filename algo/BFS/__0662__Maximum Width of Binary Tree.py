# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # BFS with index; next is cur multiplies two [O(N): 69%]
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxWidth = 0
        deq = collections.deque([(root, 0)])
        while deq:
            width = deq[-1][1] - deq[0][1] + 1
            for _ in range(len(deq)):
                cur, idx = deq.popleft()
                if not cur:
                    continue
                if cur.left:
                    deq.append((cur.left, 2*idx))
                if cur.right:
                    deq.append((cur.right, 2*idx+1))
            maxWidth = max(maxWidth, width)
        return maxWidth
    
    # =====================================

    # BFS with index [Incorrect]
    def widthOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        deq = collections.deque([(root, 0)])
        while deq:
            width = deq[-1][1] - deq[0][1]
            for _ in range(len(deq)):
                cur, idx = deq.popleft()
                if not cur:
                    continue
                if cur.left:
                    deq.append((cur.left, idx-1))
                if cur.right:
                    deq.append((cur.right, idx+1))
            maxWidth = max(maxWidth, width)
        return maxWidth
    
    # =====================================
    # BFS with dummy node [TLE]
    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        deq = collections.deque([root])
        
        start = True
        while deq:
            start = False
            for i in range(len(deq)):
                cur = deq.popleft()
                if not cur:
                    deq.append(None)
                    deq.append(None)
                    continue
                
                deq.append(cur.left)
                deq.append(cur.right)
                
                if not start:
                    leftMost = i
                    start = True
                rightMost = i
                
            width = rightMost - leftMost + 1
            maxWidth = max(maxWidth, width)
            
            if not start: #all nodes are None in this row
                break
                
        return maxWidth