class Solution:

    # Backtracking [64%]
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return 0
        
        ans = []
        used = [0] * len(nums)         #need a used array
        self.dfs(nums, [], used, ans)  #index is not needed 
        return ans
    
    def dfs(self, nums, cur, used, ans):
        if len(cur) == len(nums):
            ans.append(cur)
            return 
        
        for i in range(len(nums)):
            if used[i] == 1:
                continue
            used[i] = 1
            self.dfs(nums, cur + [nums[i]], used, ans)
            used[i] = 0