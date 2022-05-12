class Solution:
    
    # Incorrect 
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        print("Code3")
        
        def dfs(nums, idx, cur, res, visited):
            if idx in visited:
                return
            if len(cur) == len(nums):
                res.append(list(cur))
                return 
            if idx > 0 and nums[idx] == nums[idx-1] and idx - 1 not in visited:
                return
            visited.add(idx)
            cur.append(nums[idx])
            for i in range(len(nums)):
                dfs(nums, i, cur, res, visited)
            cur.remove(nums[idx])
            visited.remove(idx)
            
        nums.sort()
        res = []
        visited = set()
        dfs(nums, 0, [], res, visited)
        return res
    
    '''
    (1) sort 
    
    (2) set去重 + loop 
        TC = O(N! * 1 + N!) 
        
    (3) counter 
    
    (4) set去重 + swap
        TC = O(N! * logN + N!) 
        SC = O(N + N!)
    '''
    
    # 不盡相異物排列
    # 4 * 3 * 2 * 1 
        
    # 2022/05/12
    # Backtracking 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        print("Code2")
        
        def dfs(nums, cur, res, visited):
            if len(cur) == len(nums):
                res.append(list(cur))
                return 
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                    continue
                visited.add(i)
                dfs(nums, cur + [nums[i]], res, visited)
                visited.remove(i)
            
        nums.sort()
        res = []
        visited = set()
        dfs(nums, [], res, visited)
        return res
        
        
    
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