class Solution:
    
    # 2022/05/09
    # BFS 一次做一批，漸漸增加 [TC: O(N4^1+N4^2+..+N4^N): 76% / SC: O(N4^1+N4^2+..+N4^N): 31%]
    def letterCombinations(self, digits: str) -> List[str]:
        print("Code5: BFS")
        if not digits:
            return []
        key_map = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        ans = ['']
        for d in digits:
            new_ans = [x+y for x in ans for y in key_map[int(d)]]
            ans = new_ans
        return ans

    # 2022/05/09
    # BFS 一次做一批，漸漸增加 [TC: O(N4^1+N4^2+..+N4^N): 76% / SC: O(N4^1+N4^2+..+N4^N): 31%]
    def letterCombinations4(self, digits: str) -> List[str]:
        print("Code4: BFS")
        dToCh = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0:
            return []
        res = [ch for ch in dToCh[digits[0]]] 
        for i in range(1, len(digits)):
            d = digits[i]
            resKeep = list(res)
            res = []
            for r in resKeep:
                for ch in dToCh[d]:
                    res.append(r + ch)
        return res
    
    # 2022/05/09 
    # DFS (Backtracking) [TC:O(N * 4^N):51% / SC:O(N):31%]
    def letterCombinations3(self, digits: str) -> List[str]:
        print("Code3: DFS")
        dToCh = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def dfs(idx, cur):
            
            if idx == len(digits):
                self.res.append(''.join(cur))
                return 
            
            for ch in dToCh[digits[idx]]:
                dfs(idx + 1, cur + [ch])
        if len(digits) == 0:
            return []
        dfs(0, [])
        return res
    
    
                        
    # 2022/04/28 
    # DFS, backtracking [O(N*4^N): 37% / O(N): 32%]
    def letterCombinations2(self, digits: str) -> List[str]:
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