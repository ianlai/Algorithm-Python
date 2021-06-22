# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        results = []
        deq = collections.deque([root])
        while deq:
            maxInLayer = -float('inf')
            for _ in range(len(deq)):
                cur = deq.popleft()
                maxInLayer = max(maxInLayer, cur.val)
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            results.append(maxInLayer)
        return results
            