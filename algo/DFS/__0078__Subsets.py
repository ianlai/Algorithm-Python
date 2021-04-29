class Solution:
    
    # Backtracking [48%]
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            