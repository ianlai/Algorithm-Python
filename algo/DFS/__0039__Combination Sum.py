class Solution:

    # Backtracking [O(n^(target/min)): 63%]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []
        
        res = []
        self.backtracking(candidates, target, 0, [], res)
        return res
    
    def backtracking(self, candidates, target, idx, cur, res):
        if target == 0:
            res.append(cur)
            return
        if target < 0:
            return 
            
        for i in range(idx, len(candidates)):
            chosen = candidates[i]
            self.backtracking(candidates, target - chosen, i, cur + [chosen], res)
    
    # ==============================================================
    
    # Backtracking [48%]
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None or len(candidates) == 0:
            return []
        
        ans = []
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    def dfs(self, candidates, target, idx, cur, ans):
        if target == 0:
            ans.append(cur)
            return 
        if target < 0: 
            return 
        print(cur, target)
        for i in range(idx, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, cur + [candidates[i]], ans)