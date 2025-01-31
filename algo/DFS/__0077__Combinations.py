class Solution: 
    
    # 2022/01/24
    # Backtracking, using new cur every round [O(k * C(n, k)): 12%]
    def combine(self, n: int, k: int) -> List[List[int]]:
        print("Code3")
        def backtracking(n, k, cur, idx, res):
            if len(cur) == k:
                res.append(list(cur))
            for i in range(idx, n):
                backtracking(n, k, cur + [i+1], i+1, res)
        res = []
        backtracking(n, k, [], 0, res)
        return res
        
    # =======================================

    # 2022/01/24
    # Backtracking, using same cur until last [O(k * C(n, k)): 8%]
    def combine2(self, n: int, k: int) -> List[List[int]]:
        print("Code2")
        def backtracking(n, k, cur, idx, res):
            if len(cur) == k:
                res.append(list(cur))
            for i in range(idx, n):
                cur.append(i+1) #add (position:i, number: i+i)
                backtracking(n, k, cur, i+1, res)
                cur.remove(i+1)  
            
        res = []
        backtracking(n, k, [], 0, res)
        return res
        
    # =======================================
    
    # 2021/04/30 
    def combine1(self, n: int, k: int) -> List[List[int]]:
        print("Code1")
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
        