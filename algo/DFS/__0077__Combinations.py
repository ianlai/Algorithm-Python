class Solution:
    
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
        