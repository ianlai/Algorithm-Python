# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        idxToList = collections.defaultdict(list)
        self.traverse(root, idxToList, 0, 0, "0")
        res = []
        for idx in sorted(idxToList.keys()):
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
        
        
        