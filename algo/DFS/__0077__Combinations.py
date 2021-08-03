class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0:
            return []
        
        res = [] 
        self.dfs(n, k, 0, [], res)
        return res
    
    def dfs(self, n, k, idx, cur, res):
        if len(cur) == k :
            res.append(cur)
            return 
        
        for i in range(idx+1, n+1):
            self.dfs(n, k, i, cur + [i], res)

    # ========================================  

    # Backtracking [30%]
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0:
            return []
        
        ans = []
        self.backtracking(n, k, 0, [], ans)
        return ans
    
    def backtracking(self, n, k, idx, cur, ans):
        if len(cur) == k:
            ans.append(cur)
            return 
        
        for i in range(idx, n):
            self.backtracking(n, k, i + 1, cur + [i + 1], ans)
        