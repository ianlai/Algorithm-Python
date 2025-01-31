# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/09 
    # BFS without sorting [O(N): 66%]
    def verticalOrder(self, root):
        print("*** Code4 - BFS without sorting")
        if root is None:
            return []
        colToNodes = collections.defaultdict(list) #[value]
        deq = collections.deque([[root, 0]])       #[node, col]
        minCol, maxCol = 0, 0
        while deq:
            node, col = deq.popleft()
            if node:
                colToNodes[col].append(node.val)
                minCol = min(minCol, col)
                maxCol = max(maxCol, col)
                deq.append([node.left, col-1])
                deq.append([node.right, col+1])
        res = []
        for col in range(minCol, maxCol + 1):
            res.append(colToNodes[col])
        return res
    #======================================
    # 2022/04/09 
    # DFS [O(N): 66%]
    # (1) col order maintained by range(minCol, maxCol+1)  
    # (2) row order is sorted (at the same time keep left nodes should be first)
    # (3) left/right order is maintained by the DFS order dfs(left) -> dfs(right)
    def verticalOrder(self, root):
        if root is None:
            return []
        print("** Code3 - DFS") 
        idxToNode = collections.defaultdict(list)
        minCol, maxCol = 0, 0
        
        def dfs(node, col, row, idxToNode):
            if node is None:
                return
            idxToNode[col].append((row, node))
            nonlocal minCol, maxCol
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            dfs(node.left,  col - 1, row + 1, idxToNode)
            dfs(node.right, col + 1, row + 1, idxToNode)
        
        dfs(root, 0, 0, idxToNode)
        res = []
        for col in range(minCol, maxCol + 1):
            res.append([record[1].val for record in sorted(idxToNode[col], key = lambda x: x[0])])
        return res
        
    #======================================
    # 2021/08/10 
    # BFS with sort[O(N + NlogN): 87%]
    # - BFS keeps vertical order by nature 
    # - We sort the keys to get the horizontal order 
    def verticalOrder2(self, root):
        print("** Code2 - BFS")
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]

    #======================================
    # 2021/07/20 
    # DFS [O(N + WlogW * HlogH): 37%]
    # - col order: sort
    # - row order: sort
    # - left/right order: sort (by adding string )
    def verticalOrder1(self, root: TreeNode) -> List[List[int]]:
        print("Code1 - DFS")
        idxToList = collections.defaultdict(list)
        self.traverse(root, idxToList, 0, 0, "")
        res = []

        for idx in sorted(idxToList.keys()):  #sort by idx
            curList = idxToList[idx]
            curList.sort()
            sortedList = [e[2] for e in curList]
            res.append(sortedList)
        return res
            
    def traverse(self, root, imap, idx, depth, left):
        if not root:
            return
        imap[idx].append([depth, left, root.val])
        self.traverse(root.left,  imap, idx-1, depth+1, left + "0")
        self.traverse(root.right, imap, idx+1, depth+1, left + "1")
        
        
        