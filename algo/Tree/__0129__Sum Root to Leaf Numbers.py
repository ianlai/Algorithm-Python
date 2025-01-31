# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/26
    # Preorder DFS [O(n): 73% / O(h): 21%]
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        print("Code2")
        
        def dfs(node, cur, numbers):
            if node.left is None and node.right is None:
                numbers.append(list(cur))
            if node.left:
                cur.append(str(node.left.val))
                dfs(node.left, cur, numbers)
                cur.pop()
            if node.right:
                cur.append(str(node.right.val))
                dfs(node.right, cur, numbers)
                cur.pop()
            
        if root is None:
            return 0
        
        numbers = []
        res = 0
        dfs(root, [str(root.val)], numbers)
        for num in numbers:
            res += int("".join(num))
        return res
        
    # =================================================
    # 2021/10/19 
    # Recursive DFS [Time O(N): 71% ; Space O(H): 49% ]
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        print("Code1")
        arr = self.helper(root)
        res = 0
        for path in arr:
            res += int(path)
        return res
    def helper(self, root):
        arr = []     
        if not root.left and not root.right:
            arr.append(str(root.val))
        else:
            if root.left:
                leftArr = self.helper(root.left)
                for left in leftArr:
                    arr.append(str(root.val) + left)
            if root.right:
                rightArr = self.helper(root.right)   
                for right in rightArr:
                    arr.append(str(root.val) + right)
        return arr