# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n), 67%]
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        result = []
        if root.left or root.right:
            self.dfs(root, [], result)    #more than 1 
        else:
            result.append(str(root.val))  #only 1
            
        return result 
        
    def dfs(self, root, cur, result):
        cur.append(root.val)

        if not root.left and not root.right:
            result.append("->".join([str(element) for element in cur]))
            return
        
        if root.left:
            self.dfs(root.left, cur, result)
            cur.pop()
            
        if root.right:
            self.dfs(root.right, cur, result)
            cur.pop()
            
        
        