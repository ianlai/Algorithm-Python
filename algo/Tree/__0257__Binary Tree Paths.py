# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #2022/04/27
    #DFS (backtracking) [O(n): 55% / O(h): 30%]
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        print("Code3")
        def dfs(node, cur, res):
            cur.append(str(node.val))
            if node.left is None and node.right is None:
                res.append(list(cur))
                cur.pop()
                return 
            if node.left:
                dfs(node.left, cur, res)
            if node.right:
                dfs(node.right, cur, res)
            cur.pop()
        
        if root is None:
            return []
        
        resStr, resList = [], [] 
        dfs(root, [], resList)
        for path in resList:
            resStr.append("->".join(path))
        return resStr
    
    #DFS (backtracking) [O(n): 68% / O(h): 77%]
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        print("Code2")
        def dfs(node, cur, res):
            if node.left is None and node.right is None:
                res.append(list(cur + [str(node.val)]))
                return 
            
            cur.append(str(node.val))            
            if node.left:
                dfs(node.left, cur, res)
            if node.right:
                dfs(node.right, cur, res)
            cur.pop()
        
        if root is None:
            return []
        
        resStr, resList = [], [] 
        dfs(root, [], resList)
        for path in resList:
            resStr.append("->".join(path))
        return resStr
    
    #2021/05/15
    #DFS (backtracking) [O(n): 68% / O(h): 77%]
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        print("Code1")
        if not root:
            return []
        result = []
        
        if root.left or root.right:
            self.dfs(root, [], result)
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