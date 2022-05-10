class Solution:
    '''
    TC: O(9^k) -> O( C(9,K) ) = O(9!/(9-k)!/k!)
    SC: O(k)
    '''
    # 2022/05/10
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        print("Backtracking - func")
        target = n
        if not 0 < target <= 45 :
            return []
        
        res = []
        def dfs(digit, target, k, cur):
            if target == 0 and k == 0:
                nonlocal res
                res.append(list(cur))
                return 
            if target < 0 or k == 0:
                return 
            for nxt in range(digit + 1, 10):
                dfs(nxt, target - nxt, k - 1, cur + [nxt])
                
        dfs(0, target, k, [])
        return res 
    
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        print("Backtracking - for loop")
        target = n
        if target > 45 or target < 0:
            return []
        
        res = []
        def dfs(digit, target, k, cur):
            for nxt in range(digit + 1, 10):
                if target == nxt and k == 1:
                    nonlocal res
                    res.append(list(cur + [nxt])) 
                    continue
                if target < 0 or k == 0:
                    continue  
                dfs(nxt, target - nxt, k - 1, cur + [nxt])
                
        dfs(0, target, k, [])
        return res 
    
    # ====================================  

    # DFS [O((9!)/k!(9-k)!), 96%]
    # DFS loop has (9 - layer) choices 
    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        print("Choose different number in each layer (which)")
        if k == 0 or n == 0:
            return []
        
        results = []
        # 1 ~ 9 => [0] ~ [8]
        self.dfs(k, n, 0, [], results)
        return results
    
    def dfs(self, k, n, idx, cur, results):
        if len(cur) == k:
            if n == 0:
                results.append(cur)
            return 
        
        for i in range(idx, 9):
            val = i + 1 
            self.dfs(k, n - val, i + 1, cur + [val], results)

    # ====================================  
    
    # DFS [O((9!)/k!(9-k)!), 63%]
    # DFS loop has Yes/No choices 
    def combinationSum30(self, k: int, n: int) -> List[List[int]]:
        print("Choose take it or not in each layer (Yes/No)")
        if k == 0 or n == 0:
            return []
        
        results = []
        # 1 ~ 9 => [0] ~ [8]
        self.dfs2(k, n, 0, [], results)
        return results
    
    def dfs2(self, k, n, idx, cur, results):
        if idx > 9:
            return 
        if len(cur) > k:
            return 
        
        print(cur)
        if len(cur) == k:
            if n == 0:
                results.append(cur)
                return
        
        val = idx + 1
        if idx == 9:
            print("  idx=", idx, " val=", val)
        self.dfs2(k, n, idx + 1, cur, results)
        self.dfs2(k, n - val, idx + 1, cur + [val], results)