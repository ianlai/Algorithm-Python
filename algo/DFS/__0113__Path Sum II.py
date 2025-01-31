# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # 2022/05/07
    # Backtracking (在dfs內處理當層，代表進入迴圈的時候還沒扣好)
    # [TC: O(N2) / SC: O(N)]
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        print("Code3")
        def dfs(root, target, cur, res):
            if root is None:
                return 
            if not root.left and not root.right and root.val == target:
                cur.append(root.val)
                res.append(list(cur))
                return
            dfs(root.left , target - root.val, cur + [root.val], res)
            dfs(root.right, target - root.val, cur + [root.val], res)
        
        res = []
        if root:
            dfs(root, targetSum, [], res)
        return res
    
    # 2022/04/03 
    # Backtracking (在dfs內處理下一層，代表進入迴圈的時候已經扣好了)
    def pathSum2(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        print("Code2")
        res = []
        def dfs(root, target, cur, res):
            assert root 
            if root.left is None and root.right is None:
                if target == 0:
                    res.append(list(cur))
                return 
            if root.left:
                dfs(root.left , target - root.left.val, cur + [root.left.val], res)
            if root.right:
                dfs(root.right, target - root.right.val, cur + [root.right.val], res)
        if root:
            dfs(root, targetSum - root.val, [root.val], res)
        return res
    
    # 2021/05/03
    def pathSum1(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        print("Code1")
        if not root:
            return []
        ans = []
        self.dfs(root, targetSum - root.val, ans, [root.val])
        return ans
    
    def dfs(self, root, targetSum, ans, cur):
        if not root.left and not root.right:
            if targetSum == 0:
                ans.append(cur)
            return 
        if root.left:
            lVal = root.left.val
            self.dfs(root.left, targetSum - lVal, ans, cur + [lVal])
        if root.right:
            rVal = root.right.val
            self.dfs(root.right, targetSum - rVal, ans, cur + [rVal])
        return 