# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Inorder traversal to get the sorted array ; use return val [O(n), 6%]
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        print("Inorder, recursion, return val")
        if not root:
            return None
        return self.inorder2(root)[k-1]
            
    def inorder2(self, node):
        return self.inorder2(node.left) + [node.val] + self.inorder2(node.right) if node else []
        
    # =========================================================
    
    # Inorder traversal to get the sorted array ; use list argument [O(n), 53%]
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        print("Inorder, recursion, list argument")
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
        
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         if not root:
#             return None
#         return self.inorder(root, k, [0])    
#     def inorder(self, node, k, idx):
#         if not node:
#             return -1 
#         print(idx[0], ":", node.val)    
#         if self.inorder(node.left, k, idx) == -1:
#             return -1
#         if k == idx[0]:
#             return node.val
#         idx[0] += 1
#         if k == idx[0]:
#             return node.val
#         self.inorder(node.right, k, idx)