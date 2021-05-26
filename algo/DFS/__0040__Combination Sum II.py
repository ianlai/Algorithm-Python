class Solution:
    
    # DFS, remove redundancy before the recursion [O(2^n), 28%] 
    #
    # 1. Combination類型，所以需要紀錄idx
    # 2. 但因為需要去重，所以又必須紀錄visited[] //一般Permutation會需要紀錄visited[]
    # 3. visited[] 要跟candidates[] 等長，是要紀錄位置，而不是紀錄數值
    #    - visited.add(candidates[i]) //x
    #    - visited[i] = True          //o
    # 4. 去重: 
    #    - if i > 0 and candidates[i] == candidates[i-1] and visited[i-1] == False
    # 5. 因為每次i都從idx+1開始，所以讓一開始的idx為-1，這樣第一個迴圈就是從i=0開始取
    # 6. 把result改成set雖然在小資料時也可以過，但因為在產生答案時才去重，當重複很多時就會TLE (e.g. [2,2,2,2,2,2,2,2] 10)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Remove redundancy before the recursion")
        if not candidates:
            return []
        
        candidates.sort()
        result = []
        visited = [False] * len(candidates)
        print(candidates)
        self.dfs(candidates, target, -1, [], result, visited)
        return result
    
    def dfs(self, candidates, target, idx, cur, result, visited):
        if target < 0:
            return 
        if target == 0: 
            #result.add(tuple(cur))
            result.append(cur)
            return
        
        for i in range(idx + 1, len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1] and visited[i-1] == False: #remove redundancy 
                continue
            visited[i] = True
            self.dfs(candidates, target - candidates[i], i, cur + [candidates[i]], result, visited)
            visited[i] = False
    
    # =============================================
    
    # DFS, remove redundancy after the recursion [TLE]
    def combinationSum21(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Remove redundancy after the recursion [TLE]")
        if not candidates:
            return []
        
        candidates.sort()
        result = set()
        #visited = [False] * len(candidates)
        print(candidates)
        self.dfs1(candidates, target, -1, [], result)
        return list(result)
    
    def dfs1(self, candidates, target, idx, cur, result):
        if target < 0:
            return 
        if target == 0: 
            result.add(tuple(cur))
            #result.append(cur)
            return
        
        for i in range(idx + 1, len(candidates)):
            #if i > 0 and candidates[i] == candidates[i-1] and visited[i-1] == False: #remove redundancy 
            #    continue
            #visited[i] = True
            self.dfs1(candidates, target - candidates[i], i, cur + [candidates[i]], result)
            #visited[i] = False