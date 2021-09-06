# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # BFS + it's complete tree if any not-none after a None [O(n): 95%]
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        print("BFS + it's complete tree if any not-none after a None")
        deq = collections.deque([root])
        while deq:
            cur = deq.popleft()
            if not cur:
                if any(deq):
                    return False
                return True
            deq.append(cur.left)
            deq.append(cur.right)
        return True #will not fall into this (must encounter a None before completing the BFS)
            
    # ====================================================
    # BFS + calculate by index [O(n): 29%]
    def isCompleteTree1(self, root: Optional[TreeNode]) -> bool:
        print("BFS + calculate by index")
        if not root:
            return True
        
        deq = collections.deque([(root, 0)])
        layer = -1
        while deq:
            lastIdx = -1
            lastLayer = True
            layer += 1 
            numOfLayer = len(deq) 
            
            for _ in range(numOfLayer):
                cur, idx = deq.popleft()
                
                if cur.left:
                    deq.append((cur.left, idx*2))
                    lastLayer = False
                if cur.right:
                    deq.append((cur.right, idx*2+1))
                    lastLayer = False
                
                # check 
                if lastLayer:
                    if idx != lastIdx + 1:
                        return False
                    lastIdx = idx
                else:
                    if 2 ** layer != numOfLayer:
                        return False
        return True
                