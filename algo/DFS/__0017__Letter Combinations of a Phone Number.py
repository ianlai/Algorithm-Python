class Solution:
    
    # Backtracking [O(4^N), 94%]
    def letterCombinations(self, digits: str) -> List[str]:
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