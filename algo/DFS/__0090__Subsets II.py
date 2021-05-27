class Solution:
    
    # DFS, redundancy removal [O(2*n), 73%]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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