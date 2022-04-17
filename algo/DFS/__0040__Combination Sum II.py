class Solution:
    
    # 2022/04/17
    # Backtracking + Counter traverse (no sorting) [Time:O(2^N):78% / Space:O(N+N+N)=O(N):6%]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Code4 - Traverse count")
        
        if len(candidates) == 0:
            return []
        
        def backtracking(cur, res, countList, countIdx, target):
            if target == 0:
                res.append(list(cur))
                return 
            elif target < 0:
                return 
            for i in range(countIdx, len(countList)):
                if countList[i][1] <= 0:
                    continue
                element, count = countList[i]
                countList[i][1] = count - 1
                backtracking(cur + [element], res, countList, i, target - element)
                countList[i][1] = count
        
        countMap = collections.Counter(candidates)
        countList= [[element, count] for element, count in countMap.items()]
        res = []
        backtracking([], res, countList, 0, target)
        return res
        
    # =============================================

    # 2022/04/17
    # Backtracking + Element traverse [Time:O(NlogN + 2^N):56% / Space:O(N):23%]
    def combinationSum23(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Code3 - Traverse each element (Index)")
        
        if len(candidates) == 0:
            return []
        
        def backtracking(cur, res, idx, target, used):
            if target == 0:
                res.append(list(cur))
                return 
            elif target < 0:
                return
            
            for i in range(idx+1, len(candidates)):
                # i can be used only when i-1 is used 
                if i > 0 and candidates[i-1] == candidates[i] and not used[i-1]:
                    continue
                used[i] = True
                backtracking(cur + [candidates[i]], res, i, target - candidates[i], used)
                used[i] = False
                
        candidates.sort()
        res = []
        used = [False] * len(candidates)
        backtracking([], res, -1, target, used) #positional argument
        #backtracking(cur = [], res = res, idx = -1, target = target, used = used) #keyword argument

        return res
            
    # =============================================

    # 2021/05/27 
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

    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        print("Code2: Remove redundancy before the recursion")
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
        print("Code1: Remove redundancy after the recursion [TLE]")
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