# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/08
    # DFS + Two Pointer [O(M+N): 84%]
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(root, arr):
            if root is None:
                return 
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)
            
        def merge(arr1, arr2):
            arr3 = []
            p1, p2 = 0, 0 
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= arr2[p2]:
                    arr3.append(arr1[p1])
                    p1 += 1
                else:
                    arr3.append(arr2[p2])
                    p2 += 1
            if p1 < len(arr1):
                arr3.extend(arr1[p1:])
            elif p2 < len(arr2):
                arr3.extend(arr2[p2:])
            return arr3
        
        arr1, arr2 = [], []
        traverse(root1, arr1)
        traverse(root2, arr2)
        
        return merge(arr1, arr2)