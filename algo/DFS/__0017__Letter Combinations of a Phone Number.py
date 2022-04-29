class Solution:
    
    # 2022/04/28 
    # DFS, backtracking [O(): 37% / O(): 32%]
    def letterCombinations(self, digits: str) -> List[str]:
        print("Code2")

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def dfs(idx, cur, res):
            if idx == len(digits):
                res.append("".join(cur))
                return res
            
            for ch in digitToChar[digits[idx]]:
                cur.append(ch)
                dfs(idx+1, cur, res)
                cur.pop()
                
        if not digits:
            return []
        
        res = []
        dfs(0, [], res)
        return res
    
    # ==========================================
    # 2021/05/03 
    # Backtracking [O(4^N), 94%]
    def letterCombinations1(self, digits: str) -> List[str]:
        print("Code1")
        if len(digits) == 0:
            return []
        dToM = {
            "2": "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz" 
        }
        ans = []
        self.backtracking(digits, dToM, 0, [], ans)
        return ans
    
    def backtracking(self, digits, dToM, idx, cur, ans):
        if idx == len(digits):
            ans.append("".join(cur))
            return
        
        numberOfChar = len(dToM[digits[idx]])
        for i in range(numberOfChar):
            char = dToM[digits[idx]][i]
            self.backtracking(digits, dToM, idx + 1, cur + [char], ans)  