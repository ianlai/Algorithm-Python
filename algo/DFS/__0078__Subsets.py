class Solution:
    
    # 2022/01/24 
    # Backtracking, split to n element in each step [O(n * 2^n): 17%]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        print("Code3")
        def backtracking(nums, cur, idx, res):
            if idx == len(nums):
                return 
            
            for i in range(idx, len(nums)):
                res.append(cur + [nums[i]])
                backtracking(nums, cur + [nums[i]], i + 1, res)
        
        res = [[]]
        backtracking(nums, [], 0, res)
        return res
        
    #=========================================================

    # 2021/05/27
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        print("Code2")
        if not nums:
            return []
        
        results = []
        self.dfs(nums, -1, [], results)
        return results
    
    def dfs(self, nums, idx, cur, results):
        results.append(cur)
        
        for i in range(idx + 1, len(nums)):
            self.dfs(nums, i, cur + [nums[i]], results)
            
    #=========================================================

    # 2021/04/30
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        print("Code1")
        if not nums:
            return []
        ans = []
        self.backtracking(nums, 0, [], ans)
        return ans
    
    def backtracking(self, nums, idx, cur, ans):
        # 1. No extra exiting condition (existing condition is when idx == len(nums))
        # 2. Add cur to ans for every step (not only leaf nodes)
        ans.append(cur)
        
        for i in range(idx, len(nums)):
            self.backtracking(nums, i + 1, cur + [nums[i]], ans)