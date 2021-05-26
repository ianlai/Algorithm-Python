class Solution:
    
    # DFS [O(n!), 65%]
    # 去重的部分要特別注意，必須要事先去重，而不要事後才去重。
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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