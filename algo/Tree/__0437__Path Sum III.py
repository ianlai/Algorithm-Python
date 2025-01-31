# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # DFS [O(n), 31%]
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        
        sumList = []
        sumToCount = {}
        
        self.dfs(root, sumList, sumToCount)
        
        # Debug: 
        # keys = sorted(sumToCount)
        # for key in keys:
        #     print(key, " : ", sumToCount[key])
        
        return sumToCount[targetSum] if targetSum in sumToCount else 0
    
    def dfs(self, root, sumList, sumToCount):
        if not root:
            return 
        
        nextSumList = [root.val]
        
        # create nextSumList
        for s in sumList:
            nextSum = s + root.val
            nextSumList.append(nextSum)
            
        # count nextSumList
        for nextSum in nextSumList:
            if nextSum in sumToCount:
                sumToCount[nextSum] += 1
            else:
                sumToCount[nextSum] = 1
        
        #print("   1 ", root.val, nextSumList)
        self.dfs(root.left,  nextSumList, sumToCount)  # we don't need to create a new list because we don't modify the original list (sumList)
                                                       # so, nextSumList + [] is not needed 
        #print(">>>2 ", root.val, nextSumList)
        self.dfs(root.right, nextSumList, sumToCount)
        return 
            