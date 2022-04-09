# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/09
    # BFS [O(N + HlogH): 88%]
    # L0314 是 (col, row)相等的時候要照left/right順序排，這題是要照數值大小排。
    # 因為是用數值大小排，所以本來BFS可以自然保持row序和left/right序，在這題好處就比較少。
    # col序: 用range(min, max)
    # row序: L31做sort
    # val序: L33做sort 
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        colToRowNode = collections.defaultdict(lambda: collections.defaultdict(list))        
        deq = collections.deque([[0, 0, root]])
        minCol, maxCol = 0, 0
        while deq:
            col, row, node = deq.popleft()
            if node is None:
                continue
            colToRowNode[col][row].append(node.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            deq.append([col-1, row+1, node.left])
            deq.append([col+1, row+1, node.right])
        
        res = []
        for col in range(minCol, maxCol+1):
            cur = []
            for row in sorted(colToRowNode[col].keys()): 
                cur.extend(sorted(colToRowNode[col][row]))
            res.append(cur)
        return res
            
        
        