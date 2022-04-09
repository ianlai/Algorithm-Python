# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 2022/04/09
    # BFS, record when changing level [O(n): 40%]
    def findBottomLeftValue(self, root: TreeNode) -> int:
        print("Code2")
        if root is None:
            return -1
        deq = collections.deque([(root, 0)])
        lastLevel = 0
        res = root.val
        while deq:
            node, level = deq.popleft()
            if level != lastLevel:
                res = node.val
            if node.left:
                deq.append((node.left, level+1))
            if node.right:
                deq.append((node.right, level+1))
            lastLevel = level
        return res
        
        
    # 2021/08/02
    # BFS, one level by for loop  [O(n): 40%]
    def findBottomLeftValue1(self, root: TreeNode) -> int:
        print("Code1")
        if not root:
            return -1
        
        deque = collections.deque([root])
        ans = 0
        while deque:
            for i in range(len(deque)):
                cur = deque.popleft()
                if i == 0:
                    ans = cur.val             
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
        return ans