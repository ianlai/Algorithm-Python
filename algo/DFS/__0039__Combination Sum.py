class Solution:

    # Backtracking [56%]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
        for i in range(idx, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, cur + [candidates[i]], ans)