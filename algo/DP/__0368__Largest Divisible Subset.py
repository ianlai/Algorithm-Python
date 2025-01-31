class Solution:
    
    # 2022/04/05
    # DP [time: O(n2): 27% | space: O(n2): 37%]
    # [2,6,18] -> [2,6,18,54] as long as 54 % 18 == 0 
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % dp[j][-1] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        maxLength = 0
        maxArray = []
        for i, array in enumerate(dp):
            if len(array) > maxLength:
                maxLength = len(array)
                maxArray = array
        return maxArray
            
        
    # def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    #     nums.sort()
    #     nset = set(nums)
    #     visited = set()
    #     res = []
    #     for v in nums:
    #         if v == 1:
    #             continue
    #         count = 0
    #         cur = []
    #         nv = v
    #         while nv in nset:
    #             cur.append(nv)
    #             nv = nv * v
    #         if len(cur) > len(res):
    #             res = cur
    #     if nums[0] == 1:
    #         res.append(1)
    #     return res