# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/04/19
    # DFS + Sorted array [Time O(n) : 80% / Space O(n) : 65%]
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        print("Code2")
        sortedList = []
        self.dfs(root, sortedList)
        n = len(sortedList) 
        leftIdx, rightIdx = None, None
        
        for i in range(n-1):
            if sortedList[i].val > sortedList[i+1].val:
                leftIdx = i 
                break
        for i in reversed(range(n)):
            if sortedList[i-1].val > sortedList[i].val:
                rightIdx = i 
                break
                
        sortedList[leftIdx].val, sortedList[rightIdx].val = sortedList[rightIdx].val, sortedList[leftIdx].val
    
    def dfs(self, root, sortedList):
        if not root:
            return
        self.dfs(root.left, sortedList)
        sortedList.append(root)
        self.dfs(root.right, sortedList)
        
    # =====================================
    # 2021/08/08
    # DFS + Sorted array [Time O(n) : 96% / Space O(n) : 94%]
    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        print("Code1")
        sorted = []
        self.dfs(root, sorted)
        swap = []
        for i in range(1, len(sorted)):
            if sorted[i-1].val > sorted[i].val:
                if len(swap) == 0:
                    swap.extend([sorted[i-1], sorted[i]])  #1,3,2,4  (special case)
                elif len(swap) > 0:
                    swap.append(sorted[i])  # 1,7,3,4,5,6,2,8 
        
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val
    
    def dfs(self, root, sorted):
        if not root:
            return
        self.dfs(root.left, sorted)
        sorted.append(root)
        self.dfs(root.right, sorted)
        