class Solution:
    
    # 2021/12/05
    # Backtracking [O(n*2^n)]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        print("Code-2")
    
        def backtracking(nums, cur, res, idx, visited):
            res.append(cur)
            for i in range(idx + 1, len(nums)):
                if i > 0 and nums[i-1] == nums[i] and not visited[i-1]:
                    continue
                visited[i] = True
                #cur.append([nums[i]])
                backtracking(nums, cur + [nums[i]], res, i, visited)
                #cur.remove([nums[i]])
                visited[i] = False
        nums.sort()
        if not nums:
            return []
        visited = [False] * len(nums)
        res = []
        backtracking(nums, [], res, -1, visited)
        return res
        
        
    # ==========================================================
    # 2021/05/27
    # DFS, redundancy removal [O(2*n), 73%]
    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        results = []
        visited = [0] * len(nums)
        self.dfs(nums, 0, [], results, visited)
        return results
    
    def dfs(self, nums, idx, cur, results, visited):
        results.append(cur)
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i-1] == nums[i] and visited[i-1] == 0:
                continue
            visited[i] = 1
            self.dfs(nums, i + 1, cur + [nums[i]], results, visited)
            visited[i] = 0