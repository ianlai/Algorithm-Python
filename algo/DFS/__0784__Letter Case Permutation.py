class Solution:
    
    # DFS (backtracking) [O(2^n), 30%]
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        
        results = []
        self.dfs(s, 0, [], results)
        return results
    
    def dfs(self, s, idx, cur, results):
        if len(cur) == len(s):
            results.append("".join(cur))
            return
        
        # Note: NOT mixing loop and recursion:
        #
        # while idx < len(s) and s[idx].isdigit():
        #     cur.append(s[idx])
        #     idx += 1
        
        # Better: Use recursion for both digit and alphabet 
        if s[idx].isdigit():
            self.dfs(s, idx + 1, cur + [s[idx]], results)
        else:
            self.dfs(s, idx + 1, cur + [s[idx].upper()], results)
            self.dfs(s, idx + 1, cur + [s[idx].lower()], results)