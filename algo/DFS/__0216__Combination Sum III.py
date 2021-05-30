class Solution:
    
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
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
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
        
        #print(cur)
        if len(cur) == k:
            if n == 0:
                results.append(cur)
                return
            
        val = idx + 1
        self.dfs2(k, n, idx + 1, cur, results)
        self.dfs2(k, n - val, idx + 1, cur + [val], results)