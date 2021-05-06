# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # BFS [O(n), 65%]
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        #BFS
        deq = collections.deque([root])
        ans = []
        while deq:
            layer = []
            for _ in range(len(deq)):
                cur = deq.popleft()
                layer.append(cur.val)
                if cur.left:
                    deq.append(cur.left)
                if cur.right:
                    deq.append(cur.right)
            ans.append(layer)
        
        #Reverse 
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
                
        return ans