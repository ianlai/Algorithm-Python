# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/01/01
    # BFS
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deq = collections.deque([root])
        leavesSum = 0
        while deq:
            leavesSum = 0
            for _ in range(len(deq)):
                cur = deq.popleft()
                leavesSum += cur.val
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
        return leavesSum 
                    