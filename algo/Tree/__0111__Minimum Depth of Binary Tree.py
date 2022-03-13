# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/03/13
    # Recursion (both l and r need to be none to be leaf) [O(n): 80%]
    def minDepth(self, root: TreeNode) -> int:
        print("Code2")
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return 1 + right
        if right == 0:
            return 1 + left
        return 1 + min(right, left)
    
    # 2022/03/13
    # Recursion (incorrect; because both l and r need to be none) 
    def minDepth1(self, root: TreeNode) -> int:
        print("Code2-incorrect")
        if root is None:
            return 0
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    
    # 2021/04/22 
    # BFS [O(n): 84%]
    def minDepth(self, root: TreeNode) -> int:
        #print("Code1")
        if not root:
            return 0
        
        deq = deque([root])
        level = 1
        
        while deq:
            for i in range(len(deq)):
                cur = deq.popleft()
                if not cur.left and not cur.right:
                    return level
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
                #value doesn't matter
            level += 1 
        return level