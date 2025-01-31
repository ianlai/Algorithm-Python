class Solution:
    
    # 不盡相異物排列
    # 4 * 3 * 2 * 1 
    
    '''
    (1) sort去重 + visited 判斷填入 for 
    
    (2) sort去重 + visited 判斷填入 func 
    
    (3) set去重 + visited  
        TC = O(N! * 1 + N!) 
        
    (4) counter 
    
    (5) set去重 + swap
        TC = O(N! * logN + N!) 
        SC = O(N + N!)    
    
    (6) 條件去重 + swap

    '''
    
    #2022/05/14
    # Backtracking - counter (直接就去重，不用set，也不用額外邏輯) [O(): 55% / O(): 10%]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        print("Code6 (BEST)")    
        
        def dfs(cur, countMap):
            if len(cur) == len(nums):
                res.append(list(cur))
                return 
            for v, count in countMap.items():
                if count == 0:
                    continue
                countMap[v] -= 1
                dfs(cur + [v], countMap)
                countMap[v] += 1
            
        res = []
        dfs([], collections.Counter(nums))
        return res
    
    
    # 2022/05/14
    # Backtracking - swap + one layer visited [O(): 19% / O(): 7%]
    def permuteUnique5(self, nums: List[int]) -> List[List[int]]:
        print("Code5 (GOOD)")        
        def dfs(idx):
            print(idx, nums)
            if idx == len(nums) :
                res.append(list(nums))
                return 
            visited = set()
            for i in range(idx, len(nums)):
                #if i != idx and nums[idx] == nums[i]:  #去重
                #    continue
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
        res = []
        dfs(0)
        return res
    
    # 2022/05/14
    # Backtracking - visited + 最後才用set去重 (會最慢) [O(): 17% / O(): 47%]
    def permuteUnique4(self, nums: List[int]) -> List[List[int]]:
        print("Code4 (bad)")
        
        def dfs(cur, res, visited):
            if len(cur) == len(nums):
                res.add(tuple(cur))
                return 
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                dfs(cur + [nums[i]], res, visited)
                visited.remove(i)
        
        res = set()
        visited = set()
        dfs([], res, visited)
        return res
    
    # 2022/05/14
    # Backtracking - visited (func) [78% / 59%] 
    def permuteUnique3(self, nums: List[int]) -> List[List[int]]:
        print("Code3 (only for practice)")
        
        def dfs(nums, idx, cur, res, visited):
            if idx in visited:
                return
            if idx > 0 and nums[idx] == nums[idx-1] and idx - 1 not in visited:
                return

            #cur = cur + [nums[idx]]   #backtracking1 - 用做出新的cur的方法就不用考慮退棧(ok)
            visited.add(idx)   
            cur.append(idx)            #backtracking2 - 用idx來做成cur，保證不重複就不會退錯
            
            if len(cur) == len(nums):  #最後的判斷要在加入之後 
                res.append([nums[v] for v in cur])  #使用idx來做cur的話，最後要轉回數值
                
                cur.remove(idx)        #走進答案的情況也要退棧
                visited.remove(idx)    
                return
            
            for i in range(len(nums)):
                dfs(nums, i, cur, res, visited)
            #cur.remove(nums[idx])     #使用nums[idx]就會造成退棧退錯
            cur.remove(idx)
            visited.remove(idx)
            
        nums.sort()
        res = []
        for i in range(len(nums)):  #用func的方法就變成一開始要在外面加一層for，反而不好
            visited = set()
            dfs(nums, i, [], res, visited)
        return res
    
    # 2022/05/12
    # Backtracking - visited (for)
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        print("Code2 (GOOD)")
        
        def dfs(nums, cur, res, visited):
            if len(cur) == len(nums):
                res.append(list(cur))
                return 
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                    continue
                visited.add(i)   #index
                dfs(nums, cur + [nums[i]], res, visited) #做出新的cur傳入，沒有退棧退錯的問題
                visited.remove(i)
            
        nums.sort()
        res = []
        visited = set()
        dfs(nums, [], res, visited)
        return res
        
        
    # 2021/05/27 
    # DFS [O(n!), 65%]
    # 去重的部分要特別注意，必須要事先去重，而不要事後才去重。
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        print("Code1")
        if not nums:
            return []
        
        nums.sort()
        visited = [0] * len(nums)
        results = []
        self.dfs(nums, [], results, visited)
        return results

    def dfs(self, nums, cur, results, visited):
        if len(nums) == len(cur):
            results.append(cur)
            return 
        
        for i in range(len(nums)):
            if visited[i] == 1:
                continue
            if i > 0 and nums[i-1] == nums[i] and visited[i-1] == 0: #remove redundancy
                continue
                
            visited[i] = 1
            self.dfs(nums, cur + [nums[i]], results, visited)
            visited[i] = 0