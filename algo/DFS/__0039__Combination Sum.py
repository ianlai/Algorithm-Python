class Solution:

    # 2022/04/17
    # Backtracking [Time: O( N^(target/min +1) ) : 63% / Space: O(target/min): 60%] 
    # 樹高h = O(target/min) <- space
    # 節點數 = O( N^(target/min +1) ) <- time 
    # 時間 = 節點樹
    # 空間 = 樹深 + cur = O(target/min) + O(target/min) = O(target/min)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Code2")
        if not candidates or target <= 0:
            return []
        
        def backtracking(candidates, target, idx, cur, res):
            if target == 0:
                res.append(cur)
                return
            if target < 0:
                return 
            for i in range(idx, len(candidates)):
                backtracking(candidates, target - candidates[i], i, cur + [candidates[i]], res)

        res = []
        backtracking(candidates, target, 0, [], res)
        return res

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