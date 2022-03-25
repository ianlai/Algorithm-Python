# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    # 2022/03/25
    # Inorder traversal, iteration up to k [O(logn + k): 95%]
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        print("Code3: Inorder, iteration")
        if not root:
            return None 
            
        dummy = TreeNode(0)
        dummy.right = root
        
        stack = [dummy]
        for i in range(k):
            print(i, [node.val for node in stack])
            cur = stack.pop()
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        print(">", [node.val for node in stack])
        return stack[-1].val
    
    # =========================================================

    # 2021/05/17
    # Inorder traversal, recursion, get the whole sorted array  [O(n): 53%]
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        print("Code2: Inorder, recursion, return val")
        if not root:
            return None
        return self.inorder2(root)[k-1]
            
    def inorder2(self, node):
        return self.inorder2(node.left) + [node.val] + self.inorder2(node.right) if node else []
        
    # =========================================================
    
    # 2021/05/17
    # Inorder traversal, recursion, get the whole sorted array; use list argument [O(n), 53%]
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        print("Code1: Inorder, recursion, list argument")
        if not root:
            return None
        traversedList = []
        self.inorder1(root, traversedList)
        return traversedList[k-1]
            
    def inorder1(self, node, traversedList):
        if not node:
            return
        self.inorder1(node.left, traversedList)
        traversedList.append(node.val)
        self.inorder1(node.right, traversedList)